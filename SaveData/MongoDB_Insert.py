import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
student1={
    'id':'193131315',
    'name':'yangliu',
    'age':20,
    'gender':'male'
}
student2={
    'id':'193131314',
    'name':'aoji',
    'age':19,
    'gender':'male'
}
result=collection.insert_many([student1,student2])#只插入一条使用insert_one（）
print(result)
print(result.inserted_ids)#调用inserted_ids属性获取插入数据的_id列表