from pymongo import MongoClient
# from bson.objectid import ObjectId

class Database:
  def __init__(self):
    self._client = MongoClient('localhost', 27017)
    self._db = self._client['course-graphql']
