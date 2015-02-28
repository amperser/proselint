# -*- coding: utf-8 -*-

# Scrapy settings for newyorker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newyorker'
DOWNLOAD_DELAY = 1.00
SPIDER_MODULES = ['newyorker.spiders']
NEWSPIDER_MODULE = 'newyorker.spiders'
ITEM_PIPELINES = {
    'newyorker.pipelines.NewYorkerPipeline': 100,
}
