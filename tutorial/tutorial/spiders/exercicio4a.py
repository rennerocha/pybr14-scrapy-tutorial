import json
import re
import scrapy


class Exercicio4ASpider(scrapy.Spider):
    name = 'exercicio4a'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        raw_json = response.xpath('//script/text()').get().replace('\n', '')

        data_m = re.findall('.*var data = (\[.*\]);\s*for.*', raw_json)
        if data_m:
            quotes = json.loads(data_m.pop())

        for quote in quotes:
            yield {
                'quote': quote.get('text'),
                'author': quote.get('author').get('name'),
                'author_url': response.urljoin(
                    quote.get('author').get('goodreads_link')),
                'tags': quote.get('tags')
            }

        yield scrapy.Request(
            response.urljoin(
                response.css('.next a::attr(href)').get()
            )
        )
