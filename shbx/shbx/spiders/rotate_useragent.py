# -*-coding:utf-8-*-

"""避免被ban策略之一：使用useragent池。

使用注意：需在settings.py中进行相应的设置。
"""

import random

from scrapy import log
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

from shbx.spiders.filereader import FileReader


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            # 显示当前使用的useragent
#             print "********Current UserAgent:%s************" % ua

            # 记录
            log.msg('Current UserAgent: ' + ua, level='INFO')
            request.headers.setdefault('User-Agent', ua)

    # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape
    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = FileReader.readToList('F:\\py_scrapy\\scrapylearning\\appannie\\agents.txt')

# print(RotateUserAgentMiddleware.user_agent_list)
