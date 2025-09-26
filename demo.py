import os
import pymongo

class MongoDBClient:
    def __init__(self, database_name):
        self.client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
        self.database = self.client[database_name]
