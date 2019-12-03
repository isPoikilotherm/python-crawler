from redis import StrictRedis

redis=StrictRedis(host='localhost',port=6379,db=0,password='19961001yl')
redis.set('name','yangliu')
print(redis.get('name'))