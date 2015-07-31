# -*- coding: utf-8 -*-
import codecs
import csv


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class ShbxPipeline(object):
    def __init__(self,csvfilename):
        csvfile = file(csvfilename, 'wb')
        csvfile.write(codecs.BOM_UTF8)
        self.writer = csv.writer(csvfile, dialect='excel') 
        self.writer.writerow(['services', 'company','addrs','phoneno','extras'])
      
    def process_item(self, item, spider):
        dic = dict(item)
        
        services=ShbxPipeline.getStrFromDic(dic, 'services')
        company=ShbxPipeline.getStrFromDic(dic, 'company')
        addrs=ShbxPipeline.getStrFromDic(dic, 'addrs')
        phoneno=ShbxPipeline.getStrFromDic(dic, 'phoneno')
        extras=ShbxPipeline.getStrFromDic(dic, 'extras')
        url = ShbxPipeline.getStrFromDic(dic, 'url')
        
        self.writer.writerow([services.encode('utf-8'),
                          company.encode('utf-8'),
                          addrs.encode('utf-8'),
                          phoneno.encode('utf-8'),
                          extras.encode('utf-8'),
                          url
                          ])
        return item
    
    @staticmethod
    def getStrFromDic(dic,key):  
        astr = ''
        if dic.has_key(key):
            lst = dic[key]
            if lst:
                for tmp in lst:
                    astr += tmp+' '
        return astr
            

class DefaultPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'default.csv')
    
    def process_item(self, item, spider):
        if 'defaultPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)

class JTZXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'jtzx.csv')
    
    def process_item(self, item, spider):
        if 'jtzxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)

class GZZXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'gzzx.csv')
    
    def process_item(self, item, spider):
        if 'gzzxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        

class CJFWPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'cjfw.csv')
    
    def process_item(self, item, spider):
        if 'cjfwPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        
class RZZSPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'rzzs.csv')
    
    def process_item(self, item, spider):
        if 'rzzsPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        
class JCPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'jc.csv')
    
    def process_item(self, item, spider):
        if 'jcPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
class BJFWPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'bjfw.csv')
    
    def process_item(self, item, spider):
        if 'bjfwPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        
class JDWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'jdwx.csv')
    
    def process_item(self, item, spider):
        if 'jdwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider) 
        
class DNWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'dnwx.csv')
    
    def process_item(self, item, spider):
        if 'dnwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)      

class GDWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'gdwx.csv')
    
    def process_item(self, item, spider):
        if 'gdwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        
        
class JJWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'jjwx.csv')
    
    def process_item(self, item, spider):
        if 'jjwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)
        
class FWWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'fwwx.csv')
    
    def process_item(self, item, spider):
        if 'fwwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)

class SJWXPipeline(ShbxPipeline):
    def __init__(self):
        ShbxPipeline.__init__(self, 'sjwx.csv')
    
    def process_item(self, item, spider):
        if 'sjwxPipeLine' not in getattr(spider, 'pipelines',[]):
            return item;
        else:
            return ShbxPipeline.process_item(self, item, spider)