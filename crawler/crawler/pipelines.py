# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
import json
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MongoDBTheThao247Pipeline:
    def __init__(self):
        # Kết nối MongoDB
        self.mongo_client = pymongo.MongoClient("mongodb://mongo_db:27017/")
        self.mongo_db = self.mongo_client["TheThao247"]
        self.mongo_collection = self.mongo_db["theothao247"]
        
        # Kết nối Redis
        self.redis_client = redis.Redis(host="redis_db", port=6379, decode_responses=True)

    def process_item(self, item, spider):
        try:
            # Chuyển đổi item thành JSON
            item_json = json.dumps(dict(item))
            
            # Lưu vào Redis trước
            self.redis_client.lpush("theothao247_news", item_json)
            
            # Sau đó lưu vào MongoDB
            self.mongo_collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error processing item: {e}")
    
    def close_spider(self, spider):
        self.mongo_client.close()  # Đóng kết nối MongoDB

