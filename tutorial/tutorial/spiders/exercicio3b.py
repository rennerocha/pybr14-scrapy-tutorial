# -*- coding: utf-8 -*-
import scrapy


class Exercicio3BSpider(scrapy.Spider):
    name = 'exercicio3b'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'username', 'password': 'password'},
            callback=self.parse_logged_in
        )

    def parse_logged_in(self, response):
        for quote in response.css('.quote'):
            yield {
                'quote': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'author_url': response.urljoin(
                    quote.xpath('.//a[contains(text(), "about")]/@href').get()),
                'tags': quote.css('.tag *::text').getall(),
            }

        yield scrapy.Request(
            response.urljoin(
                response.css('.next a::attr(href)').get()
            ),
            callback=self.parse_logged_in,
        )
