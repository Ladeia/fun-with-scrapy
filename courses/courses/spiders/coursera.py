# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    start_urls = ['http://www.coursera.org/browse']

    def parse(self, response):
        self.log(response.body)
