# -*- coding: utf-8 -*-

"""Settings for the spider."""

BOT_NAME = 'newyorker'
DOWNLOAD_DELAY = 1.00
SPIDER_MODULES = ['newyorker.spiders']
NEWSPIDER_MODULE = 'newyorker.spiders'
ITEM_PIPELINES = {
    'newyorker.pipelines.NewYorkerPipeline': 100,
}
