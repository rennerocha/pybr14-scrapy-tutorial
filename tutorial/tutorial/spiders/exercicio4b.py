import js2xml
import scrapy


class Exercicio4BSpider(scrapy.Spider):
    name = 'exercicio4b'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        parsed = js2xml.parse(response.xpath('//script/text()').get())

        quotes = parsed.xpath('//var[@name="data"]/array/object')
        for quote_element in quotes:
            quote = js2xml.make_dict(quote_element)

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
