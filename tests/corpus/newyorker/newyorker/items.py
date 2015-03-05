# -*- coding: utf-8 -*-

"""Stuff to pull from a New Yorker article."""

import scrapy


class NewYorkerItem(scrapy.Item):

    """Pull the title, author, text, and link."""

    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
