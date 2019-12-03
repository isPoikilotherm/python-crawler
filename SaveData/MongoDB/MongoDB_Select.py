import pymongo
from bson.objectid import ObjectId

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.weibo
collection=db.weibo
# result=collection.find_one({'name':'yangliu'})#通过name属性值查找
# print(type(result))
# print(result)

# result1=collection.find_one({'_id':ObjectId('5de4a83c2d768837d56b714e')})#通过_id查找
# print(result1)

result2=collection.find()
result=collection.find().count()
print(result2)
for re in result2:
    print(re)
print(result)