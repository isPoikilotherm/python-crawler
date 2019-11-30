import pymysql

# id='193131315'
# user='yangliu'
# age=23
#
# db=pymysql.connect(host='localhost',user='root',password='19961001yl',port=3306,db='spiders')
# cursor=db.cursor()
# sql='insert into students(id,name,age)values (%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()#若出现异常，则执行数据回滚，相当于什么都没有发生
# db.close()


#动态插入
db=pymysql.connect(host='localhost',user='root',password='19961001yl',port=3306,db='spiders')
cursor=db.cursor()
data={
    'id':'193131314',
    'name':'aoji',
    'age':22
}
# table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into students({keys})values ({values})'.format(keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()
