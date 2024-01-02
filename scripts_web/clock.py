"""Check emails to editor@proselint.com, lint them, and reply."""

import hashlib
import json
import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import gmail
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from proselint import log
from worker import conn

logging.basicConfig()
scheduler = BlockingScheduler()

# Settings
user = "hello@lifelinter.com"
user_to = "editor@proselint.com"
name = "proselint"
password = os.environ["gmail_password"]

tagline = "Proselint, a linter for prose."
url = "http://proselint.com"
api_url = "http://api.proselint.com/v0/"


def quoted(string, every=64):
    """Insert a quote before linebreaks."""
    return "> " + re.sub("\r\n(?=[^\r\n])", "\r\n> ", string)


@scheduler.scheduled_job("interval", minutes=0.25)
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

        signature = (
            u.fr.decode("utf-8") + u.subject.decode("utf-8") + u.body.decode("utf-8")
        )

        _hash = hashlib.sha256(signature.encode("utf-8")).hexdigest()

        if user_to in u.to or user_to in u.headers.get("Cc", []):
            job_id = conn.get(_hash)

            if not job_id:
                # If the email hasn't been sent for processing, send it.
                r = requests.post(api_url, data={"text": u.body})
                conn.set(_hash, r.json()["job_id"])
                log.info("Email %s sent for processing.", _hash)

            else:
                # Otherwise, check whether the results are ready, and if so,
                # reply with them.
                r = requests.get(api_url, params={"job_id": job_id})

                if r.json()["status"] == "success":
                    reply = quoted(u.body)
                    errors = r.json()["data"]["errors"]
                    reply += "\r\n\r\n".join([json.dumps(e) for e in errors])

                    msg = MIMEMultipart()
                    msg["From"] = f"{name} <{user}>"
                    msg["To"] = u.fr
                    msg["Subject"] = "Re: " + u.subject

                    if u.headers.get("Message-ID"):
                        msg.add_header("In-Reply-To", u.headers["Message-ID"])
                        msg.add_header("References", u.headers["Message-ID"])

                    body = reply + "\r\n\r\n--\r\n" + tagline + "\r\n" + url
                    msg.attach(MIMEText(body, "plain"))

                    text = msg.as_string()
                    server.sendmail(user, u.fr, text)

                    # Mark the email as read.
                    u.read()
                    u.archive()

                    log.info("Email %s has been replied to.", _hash)


scheduler.start()
