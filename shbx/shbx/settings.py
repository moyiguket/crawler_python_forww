# -*- coding: utf-8 -*-

# Scrapy settings for shbx project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shbx'

SPIDER_MODULES = ['shbx.spiders']
NEWSPIDER_MODULE = 'shbx.spiders'

COOKIES_ENABLES=False
DOWNLOAD_DELAY=2
AJAXCRAWL_ENABLED = True
RETRY_TIMES = 2
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
CONCURRENT_REQUESTS = 100

ITEM_PIPELINES = {
    'shbx.pipelines.JTZXPipeline':300,
    'shbx.pipelines.GZZXPipeline':300,
    'shbx.pipelines.CJFWPipeline':300,
    'shbx.pipelines.RZZSPipeline':300,
    'shbx.pipelines.JCPipeline':300,
    'shbx.pipelines.BJFWPipeline':300,
    'shbx.pipelines.JDWXPipeline':300,
    'shbx.pipelines.DNWXPipeline':300,
    'shbx.pipelines.GDWXPipeline':300,
    'shbx.pipelines.JJWXPipeline':300,
    'shbx.pipelines.FWWXPipeline':300,
    'shbx.pipelines.SJWXPipeline':300,
}

#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    'shbx.spiders.randomproxy.RandomProxy': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'shbx.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
}
PROXY_LIST = 'F:\\py_scrapy\\scrapylearning\\shbx\\list.txt'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shbx (+http://www.yourdomain.com)'
