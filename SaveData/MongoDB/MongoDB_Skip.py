import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
# results=collection.find().sort('name',pymongo.ASCENDING).skip(2)#以name属性升序排序,skip(2)表示偏移两个位置，得到从第三个开始的元素
# print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)#以name属性升序排序,skip(2)表示偏移两个位置，
# limit(2)表示依次只取两个元素
print([result['name'] for result in results])