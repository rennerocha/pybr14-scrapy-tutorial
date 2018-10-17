import scrapy

class SimpleSpider(scrapy.Spider):
  name = 'simplespider'
  start_urls = ['http://scrapy.org/']

  def parse(self, response):
    self.logger.debug('Site visited: {}'.format(response.url))
    yield {'url': response.url, 'size': len(response.body)}

    next_url = 'http://python.org/'
    self.logger.debug('Next site: {}'.format(next_url)

    yield scrapy.Request(next_url, self.handle_python)

  def handle_python(self, response):
    self.logger.debug('Python site visited: {}'.format(response.url))