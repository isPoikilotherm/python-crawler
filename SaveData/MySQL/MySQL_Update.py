import pymysql

db=pymysql.connect(host='localhost',user='root',password='19961001yl',port=3306,db='spiders')
cursor=db.cursor()
data={
    'id':'193131314',
    'name':'aoji',
    'age':20
}
# table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into students({keys})values ({values})on duplicate key update '.format(keys=keys,values=values)
update=','.join(["{key}=%s".format(key=key)for key in data])
sql+=update#若存在此条记录则更新，不存在则插入，通过主键判断
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()
