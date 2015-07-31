# -*- coding: utf-8 -*-

class FileReader(object):
    '''
    classdocs
    '''
     
    @staticmethod   
    def readToList(filepath):
        lst=[]
        reader = open(filepath)
        for line in reader.readlines():
            line=line.strip()
            if not line or line.startswith(':'):
                continue
            lst.append(line)
        reader.close()
        return lst

if __name__ == '__main__':
    print(FileReader.readToList('F:\\py_scrapy\\scrapylearning\\appannie\\list.txt'))