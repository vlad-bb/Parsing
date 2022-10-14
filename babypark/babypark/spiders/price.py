import scrapy
from datetime import datetime
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging
from twisted.internet import reactor


class PriceSpider(scrapy.Spider):
    name = 'price'
    allowed_domains = ['www.babypark.de']
    start_urls = ['http://www.babypark.de']
    data = None

    def parse(self, response):

        try:

            price = response.css('span[class=price]').get()
            print(price)
            yield price

        except Exception as err:
            print(err)

        for d in self.data:
            yield scrapy.Request(url=self.start_urls[0] + d['link'])


def main(data_table):
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    # runner = CrawlerRunner()
    # d = runner.crawl(PriceSpider, data_table)
    # d.addBoth(lambda _: reactor.stop())
    # reactor.run()
    # process - method
    process = CrawlerProcess()
    process.crawl(PriceSpider, data_table)
    process.start()


if __name__ == '__main__':
    main()
