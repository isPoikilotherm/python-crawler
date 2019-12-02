import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
results=collection.find().sort('name',pymongo.ASCENDING)#以name属性升序排序,降序使用pymongo.DESCENDING
print([result['name'] for result in results])
# for result in results:
#     print(result)