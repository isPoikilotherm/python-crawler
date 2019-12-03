import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
# condition={'name':'yangliu'}
# condition_1={'name':'aoji'}
# student=collection.find_one(condition_1)
# student['age']=100
# # result=collection.update(condition,student)
# # print(result)
#
# result_1=collection.update_one(condition_1,{'$set':student})
# print(result_1)
# print(result_1.matched_count,result_1.modified_count)#matched_count匹配的条数；modified_count影响的条数


condition_2={'age':{'$gte':20}}
# result_2=collection.update_one(condition_2,{'$inc':{'age':1}})
# print(result_2)
# print(result_2.matched_count,result_2.modified_count)

result_3=collection.update_many(condition_2,{'$inc':{'age':1}})
print(result_3)
print(result_3.matched_count,result_3.modified_count)