from urllib.parse import urlunsplit

data = ['http','www.baidu.com','index.html','a=6','comment']#参数只能是五个
print(urlunsplit(data))
#将元组转化为链接