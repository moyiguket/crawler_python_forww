# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


# class ComplexItem(scrapy.Item):
class ShbxItem(scrapy.Item):
    
    services = Field()
    company = Field()
    addrs = Field()
    phoneno = Field()
    extras = Field()
    url = Field()
#     
#     freehotline = Field()
#     hotline = Field()
#     addr = Field()
#     qq = Field()
#     category = Field()
#     companyinfo = Field()
