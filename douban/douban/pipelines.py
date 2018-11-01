# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.utils.project import get_project_settings
settings = get_project_settings()


class DoubanPipeline(object):

    def __init__(self):
        self.host = settings.get('MONGO_URI')
        self.port = settings.get('MONGO_PORT')
        self.mongo_db = settings.get('MONGO_DB')

    def open_spider(self, spider):
        #创建数据库链接
        self.client = pymongo.MongoClient(self.host, self.port)
        #指定数据库的名称
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        #指定表名插入数据
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()