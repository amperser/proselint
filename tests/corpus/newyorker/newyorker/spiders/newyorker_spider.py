"""Define a spider."""

import scrapy
from newyorker.items import NewYorkerItem


class NewYorkerSpider(scrapy.Spider):

    """Visit the archives of The New Yorker and pull out articles."""

    name = "newyorker"
    allowed_domains = ["newyorker.com"]

    start_urls = []
    base_url = "http://www.newyorker.com/magazine/reporting/page/"
    for i in range(1, 182):
        start_urls.append(base_url + str(i))

    print start_urls

    def parse(self, response):
        """Get articles if any exist on this page."""
        for sel in response.xpath(
                '//article[@itemtype="http://schema.org/Article"]'):

            item = NewYorkerItem()

            item['title'] = sel.xpath(
                '//article//header/hgroup/h1/text()').extract()

            item['author'] = sel.xpath(
                '//article//header/hgroup/h3/span/a/text()').extract()

            item['text'] = sel.xpath(
                '//article//div[@class="articleBody"]//p').extract()

            yield item

        # Get full text link.
        url_selector = '//article/div[@itemprop="description"]/a/@href'
        for url in response.xpath(url_selector).extract():
            yield scrapy.Request(url, callback=self.parse)
