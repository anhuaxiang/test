from pymongo import MongoClient

client = MongoClient()

collection = client.test.test_collection

collection.insert({'a': 1, 'b': 'c'})
# collection.insert({'a': 4, 'b': 'e'})

collection.find({'a': 1, '$or': [{'b': 'b'}, {'b': 'c'}]})
collection.find({'a': {'$gt': 2}})  # gt lt gte lte
collection.find({}).sort({'b': 1})