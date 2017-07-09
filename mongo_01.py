import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.local
collection = db.col
for col in collection.find({'by': 'cainiao'}):
    print(col)
#ret = collection.insert_one({'title': 'Mysql', 'by': 'zyf'})
#print(ret.inserted_id)
for col in collection.find():
    print(col)
