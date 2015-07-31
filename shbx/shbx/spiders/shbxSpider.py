# -*- coding: utf-8 -*-
'''
@author: da.sun
'''
import re
import time
from urllib2 import HTTPError

from scrapy import log
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector.unified import Selector
from selenium import webdriver

from shbx.items import ShbxItem


class ShbxSpider(CrawlSpider):
    
    allowed_domains = ['shanghai.baixing.com']
    
    baseurl='http://shanghai.baixing.com'
    
    name='default'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/jiancaizhuangshi/a249472628.html',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/jiancaizhuangshi/a\d+\.html")),
             callback='parse_item',
             follow=True),
        
    ]

    
    pipelines = ['defaultPipeLine']
    
    def __init__(self):
        CrawlSpider.__init__(self)
        self.driver = webdriver.Firefox()
       
    def getString(self,path):
        result=''
        if path:
            for info in path:
                if isinstance(info, basestring):
                    result += info+' '
                else:
                    result += info.extract()+' '
        
        return result
    
    def replaceurl(self,url):
        url = re.sub('/m/', '', url)
        return url
    
    def noturl(self,url):
        if '/m/' in url:
            self.log('not url', level=log.DEBUG)
            return True
        return False
    
#     def parse(self, response):
#         url = response.url
# 
#         request = Request(url,callback=self.com_parse)   
#         yield request
        
#     def m_parse(self,response):
#         self.log('into m_parse', level=log.DEBUG)
#         urls =  response.xpath("//li[@class='item ace'][1]/a/@href").extract()
#         for infourl in urls:
#             self.log('info url :'+infourl)
#             request = Request(infourl, callback=self.parse_item)   
#             yield request
#         nexturls = response.xpath("//a[@class='next-page']/@href").extract()
#         if not nexturls:
#             self.log('not nexturls ')
#         for nexturl in nexturls:
#             nexturl = self.baseurl+nexturl
#             request = Request(nexturl,callback=self.parse)
#             log.msg('crawl next url '+nexturl)
#             yield request
            
    def parse(self,response):
        self.log('into parse', level=log.DEBUG)
        
        urls =  response.xpath("//div[@class='media-body-title']/a/@href").extract()
        for infourl in urls:
            self.log('info url :'+infourl)
            request = Request(infourl,meta = {
                      'dont_redirect': True,
                      'handle_httpstatus_list': [302]
                  },callback=self.parse_item)   
            yield request
        nexturls = response.xpath("//a[@class='pagenav-cell pagenav-cell-next']/@href").extract()
        if not nexturls:
            self.log('not nexturls ')
        for nexturl in nexturls:
            nexturl = self.baseurl+nexturl
            request = Request(nexturl,meta = {
                      'dont_redirect': True,
                      'handle_httpstatus_list': [302]
                  },callback=self.parse)
            log.msg('crawl next url '+nexturl)
            yield request
        
#     def m_parse_item(self, response):
#         self.log('into m_parse_item', level=log.DEBUG)
#         url = response.url
#         self.driver.get(response.url)
#         
#         selector=response
#         self.log('parse_item ,url:'+url, level=log.DEBUG)
#         item = ShbxItem()
#         service_path = selector.xpath('//dl/dd/a/text()').extract()
#         
#         services = self.getString(service_path);
#         
#         company_path = selector.xpath('//dl/dd[4]/text()')
#         company = self.getString(company_path)
#         
#         addrs_path = selector.xpath('//dl/dd[7]/text()')
#         addrs = self.getString(addrs_path)
#         
#         extras_path = selector.xpath('//dl/dd[6]/text()')
#         extras = self.getString(extras_path)
#         
#         phoneno=selector.xpath("//a[@id='contact-number']/text()").extract()
#         
#         item['services']=services
#         item['addrs'] = addrs
#         item['phoneno'] = phoneno
#         item['company'] = company
#         item['extras'] = extras
#         item['url']=url
#         yield item
        
    def parse_item(self, response):
        self.log('into parse_item', level=log.DEBUG)
        url = ''
        try:
            url = response.url
        except:
            yield ShbxItem()
            
        item = ShbxItem()
        if '/m/' in url:
            item['url']=url
            yield item()
            pass
            
          
        self.driver.get(response.url)
        
        show = self.driver.find_element_by_xpath("//a[@class='show-contact button']")
        try:
            show.click()
        except:
            pass
        
        time.sleep(3)
        
        root = self.driver.page_source
        selector=Selector(text=root)
        self.log('parse_item ,url:'+url, level=log.DEBUG)
        service_path = selector.xpath('//span[@class="normal"][1]/a/text()').extract()
        
        services = self.getString(service_path);
        service_path = selector.xpath('//span[@class="normal"][1]/text()').extract()
        services += self.getString(service_path);
        
        company_path = selector.xpath('//span[@class="long"][1]/a/text()')
        company = self.getString(company_path)
        company_path = selector.xpath('//span[@class="long"][1]/text()')
        company += self.getString(company_path)
        company_path = selector.xpath('//span[@class="long"][1]/span/text()')
        company += self.getString(company_path)
        
        addrs_path = selector.xpath('//span[@class="long"][2]/a/text()')
        addrs = self.getString(addrs_path)
        addrs_path = selector.xpath('//span[@class="long"][2]/text()')
        addrs += self.getString(addrs_path)
        addrs_path = selector.xpath('//span[@class="long"][2]/span/text()')
        addrs += self.getString(addrs_path)
        
        extras_path = selector.xpath('//span[@class="long"][3]/a/text()')
        extras = self.getString(extras_path)
        extras_path = selector.xpath('//span[@class="long"][3]/text()')
        extras += self.getString(extras_path)
        extras_path = selector.xpath('//span[@class="long"][3]/span/text()')
        extras += self.getString(extras_path)
        
        phoneno=selector.xpath('//span[@id="num"]/text()').extract()
        
        item['services']=services
        item['addrs'] = addrs
        item['phoneno'] = phoneno
        item['company'] = company
        item['extras'] = extras
        item['url']=url
        yield item


    def throwEx(self,url):
        if 'areyouhuman' in url:
            self.log('ip is banned', _level='INFO')
            
            raise HTTPError(url, 403, "robot confirm",None,None)
        

class JZSpider(ShbxSpider):
    name='jtzx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/jiatingzhuangxiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(
                               allow=(r"shanghai.baixing.com/jiatingzhuangxiu/"),
                               deny=('/m/'),
                               ),
           callback='parse_item',
           follow=True),
    ]

    pipelines = ['jtzxPipeLine']
    
class GZSpider(ShbxSpider):
    name='gzzx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/zhuangxiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(
                               allow=(r"shanghai.baixing.com/zhuangxiu/"),
                               deny=('/m/')
                            ),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['gzzxPipeLine']

class CJSpider(ShbxSpider):
    name='cjfw'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/chaijiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/chaijiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['cjfwPipeLine']

class RZSpider(ShbxSpider):
    name='rzzs'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/ruanzhuang/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/ruanzhuang/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['rzzsPipeLine']
    
class JCSpider(ShbxSpider):
    name='jc'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/jiancaizhuangshi/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/jiancaizhuangshi/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['jcPipeLine']
    
class BJSpider(ShbxSpider):
    name='bjfw'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/banjia/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/banjia/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['bjfwPipeLine']
    
class JDWXSpider(ShbxSpider):
    name='jdwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/jiadianweixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/jiadianweixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['jdwxPipeLine']

class DNWXSpider(ShbxSpider):
    name='dnwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/diannaoweixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/diannaoweixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['dnwxPipeLine']
    
class GDWXSpider(ShbxSpider):
    name='gdwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/weixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/weixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['gdwxPipeLine']
       
class JJWXSpider(ShbxSpider):
    name='jjwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/jiajuweixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/jiajuweixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['jjwxPipeLine']

class FWWXSpider(ShbxSpider):
    name='fwwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/fangwuweixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/fangwuweixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['fwwxPipeLine']
    
class SJWXSpider(ShbxSpider):
    name='sjwx'
    
    #第一篇文章地址
    start_urls = ['http://shanghai.baixing.com/shoujiweixiu/',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r"shanghai.baixing.com/shoujiweixiu/a\d+\.html")),
             callback='parse_item',
             follow=True),
    ]

    pipelines = ['sjwxPipeLine']
    