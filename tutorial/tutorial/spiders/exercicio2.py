import json
import scrapy


class Exercicio2Spider(scrapy.Spider):
    name = 'exercicio2'
    allowed_domains = ['toscrape.com']
    api_url = 'http://quotes.toscrape.com/api/quotes?page={page}'

    def start_requests(self):
        yield scrapy.Request(self.api_url.format(page=1))

    def parse(self, response):
        data = json.loads(response.body)
        actual_page = data.get('page')

        for quote in data.get('quotes'):
            yield {
                'quote': quote.get('text'),
                'author': quote.get('author').get('name'),
                'author_url': response.urljoin(
                    quote.get('author').get('goodreads_link')),
                'tags': quote.get('tags'),
            }

        if data.get('has_next'):
            next_page = actual_page + 1
            yield scrapy.Request(
                self.api_url.format(page=next_page)
            )
