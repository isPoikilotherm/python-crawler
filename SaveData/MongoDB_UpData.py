import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
condition={'name':'yangliu'}
student=collection.find_one(condition)
student['age']=99
result=collection.update(condition,student)
print(result)