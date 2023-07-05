# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BookscrapyPipeline:
    def process_item(self, item, spider):
        return item

from pymongo import MongoClient

class BookscrapyPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['smartmaple']
        self.collection = self.db['kitapyurdu']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert_one(data)
        return item
