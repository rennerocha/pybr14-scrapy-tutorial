import scrapy


class MyFirstSpider(scrapy.Spider):
  name = 'my-first-spider'

  start_urls = [
    'http://quotes.toscrape.com/page/1/',
    'http://quotes.toscrape.com/page/2/',
  ]

  def parse(self, response):
    self.logger.info('Just parsing {}'.format(response.url))

