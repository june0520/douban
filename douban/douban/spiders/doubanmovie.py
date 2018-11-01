# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            item = DoubanItem()
            item['name'] = each.xpath(".//span[@class='title'][1]/text()").extract_first()
            item['db'] = each.xpath(".//p[1]/text()").extract_first()
            item['star'] = each.xpath(".//span[@class='rating_num']/text()").extract_first()
            item['quote'] = each.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
