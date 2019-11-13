from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']#必须满足六个参数
print(urlunparse(data))