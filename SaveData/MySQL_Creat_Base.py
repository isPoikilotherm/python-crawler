import pymysql

db=pymysql.connect(host='localhost',user='root',password='19961001yl',port=3306)
cursor=db.cursor()#调用cursor（）方法获得MySQL的操作游标，利用游标来执行SQL语句
cursor.execute('SELECT VERSION()')#查看版本号
data=cursor.fetchone()#fetchone()方法获取第一条数据
print('Database version:',data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")#创建名为spiders的数据库，默认编码为utf-8
db.close()