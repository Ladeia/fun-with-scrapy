import scrapy


class AntonioLadeiaSpider(scrapy.Spider):

    name = 'ladeia'
    start_urls = ['http://www.antonioladeia.com']

    def parse(self, response):
        self.log(response.body)
