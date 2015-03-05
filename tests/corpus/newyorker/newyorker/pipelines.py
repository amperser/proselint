# -*- coding: utf-8 -*-

"""Pipeline for extracting info from New Yorker archives."""

from bs4 import BeautifulSoup
import string


class NewYorkerPipeline(object):

    """Define the pipeline."""

    def process_item(self, item, spider):
        """Process the item."""
        exclude = set(string.punctuation)
        filename = item['title'][0].lower()
        filename = ''.join(ch for ch in filename if ch not in exclude)
        filename = filename.replace(" ", "-")

        with open(filename + ".md", "a+") as f:
            f.write(item['title'][0] + "\n")
            f.write("*The New Yorker*\n")
            f.write("By " + item['author'][0] + "\n\n")

            soup = BeautifulSoup("\n".join(item["text"]))
            text = "\n".join(soup.findAll(text=True)).strip()
            text = text.replace("\n\n\n", "\n\n")
            text = text.replace("</span>", "")
            text = text.replace("\n ", "\n")
            text = text.replace('span id="incorrect">', "")
            text = text.replace("\n*\n", "*\n")
            text = text.replace('\n**\n', "**\n")
            f.write(text.encode("utf-8"))

        return item
