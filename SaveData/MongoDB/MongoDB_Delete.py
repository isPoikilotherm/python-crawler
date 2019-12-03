import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
# result=collection.remove({'name':'aiwenyu'})
# print(result)

# result_1=collection.delete_one({'name':'aiwenyu'})
# print(result_1)
# print(result_1.deleted_count)


result_2=collection.delete_many({'age':{'$lt':20}})
print(result_2)
print(result_2.deleted_count)