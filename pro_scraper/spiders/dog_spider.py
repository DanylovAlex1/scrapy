# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from pro_scraper.items import Dog



class DogsSpider(scrapy.Spider):
    name = ' olx_dogs_spider'
    allowed_domains = ['olx.ua/zhivotnye/sobaki/']
    start_urls = ['https://www.olx.ua/zhivotnye/sobaki/']


    def parse(self, response):


        l = ItemLoader(item=Dog(), response=response)

        l.add_xpath('title', "//div[@class='space rel']/h3[@class='lheight22 margintop5']/a/strong/text()")
        l.add_xpath('price', "//div[@class= 'space inlblk rel']/p[@class='price']/strong/text()")
        l.add_xpath('location', "//div[@class= 'space rel']/p[@class='lheight16']/small[@class='breadcrumb x-normal']/span/text()")
        #l.add_value('img_url', response.url,output_processor=TakeFirst())
        return l.load_item()



'''
scrapy genspider secspider mydomain.com
scrapy runspider pro_scraper/spiders/dog_spider.py -o dogs.json
'''