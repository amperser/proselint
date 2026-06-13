"""Check emails to editor@proselint.com, lint them, and reply."""

from apscheduler.schedulers.blocking import BlockingScheduler
import gmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from worker import conn
import requests
import hashlib
import json
import os
import logging
import re

logging.basicConfig()
scheduler = BlockingScheduler()

# Settings
user = "hello@lifelinter.com"
user_to = "editor@proselint.com"
name = "proselint"
password = os.environ['gmail_password']

tagline = "Proselint, a linter for prose."
url = "http://proselint.com"
api_url = "http://api.proselint.com/v0/"


def quoted(string, every=64):
    """Insert a quote before linebreaks."""
    return "> " + re.sub("\r\n(?=[^\r\n])", "\r\n> ", string)


 @scheduler.scheduled_job('interval', minutes=0.25)
def check_email():
    """Check the mail account and lint new mail."""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, password)

    g = gmail.login(user, password)

    # Check for unread messages.
    unread = g.inbox().mail(unread=True)

    # Submit a job to lint each email sent to editor@proselint.com. Record the
    # resulting job_ids somewhere (in Redis, I suppose), keyed by a hash of the
    # email.
    for u in unread:

        u.fetch()

        signature = (u.fr.decode('utf-8') +
                     u.subject.decode('utf-8') +
                     u.body.decode('utf-8'))

        hash = hashlib.sha256(signature.encode('utf-8')).hexdigest()

        if user_to in u.to or user_to in u.headers.get('Cc', []):

            job_id = conn.get(hash)

            if not job_id:
                # If the email hasn't been sent for processing, send it.
                try:
                    r = requests.post(api_url, data={"text": u.body})
                    if r.status_code == 200:
                        data = r.json()
                        job_id = data.get("job_id")
                        if job_id:
                            conn.set(hash, job_id)
                            print("Email {} sent for processing.".format(hash))
                        else:
                            logging.error("Job ID missing in API response for hash %s", hash)
                    else:
                        logging.error("API submission failed with status %d for hash %s", r.status_code, hash)
                except (requests.RequestException, json.JSONDecodeError):
                    logging.error("Failed to submit job for hash %s", hash)

            else:
                # Otherwise, check whether the results are ready, and if so,
                # reply with them.
                try:
                    r = requests.get(api_url, params={"job_id": job_id})

                    if r.status_code == 200:
                        data = r.json()
                        if data.get("status") == "success":

                            reply = quoted(u.body)
                            errors = data.get('data', {}).get('errors', [])
                            reply += "\r\n\r\n".join([json.dumps(e) for e in errors])

                            msg = MIMEMultipart()
                            msg["From"] = "{} <{}>".format(name, user)
                            msg["To"] = u.fr
                            msg["Subject"] = "Re: " + u.subject

                            if u.headers.get('Message-ID'):
                                msg.add_header("In-Reply-To", u.headers['Message-ID'])
                                msg.add_header("References", u.headers['Message-ID'])

                            body = reply + "\r\n\r\n--\r\n" + tagline + "\r\n" + url
                            msg.attach(MIMEText(body, "plain"))

                            text = msg.as_string()
                            server.sendmail(user, u.fr, text)

                            # Mark the email as read.
                            u.read()
                            u.archive()

                            print("Email {} has been replied to.".format(hash))
                        elif data.get("status") == "error":
                            logging.error("API returned error status for hash %s: %s", hash, data.get("message"))
                    else:
                        logging.error("API result check failed with status %d for hash %s", r.status_code, hash)
                except (requests.RequestException, json.JSONDecodeError):
                    logging.error("Failed to check results for hash %s", hash)


scheduler.start()
