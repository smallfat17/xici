# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import requests

class XiciPipeline(object):
    def __init__(self):
        self.client = MongoClient(host='localhost')
        self.collection = self.client.ips.xici
        self.session = requests.session()
        self.session.headers = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/60.0'}
    def process_item(self, item, spider):
        self.session.proxies = 'http://{}:{}'.format(item['host'],item['port'])
        if self.session.get('http://www.baidu.com').status_code == 200:
            self.collection.insert(dict(item))
        return item
