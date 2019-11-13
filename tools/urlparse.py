from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)#返回元组类型

result1 = urlparse('www.baidu.com/index.html;user?id=5#comment',
                   scheme='http')#返回元组类型
print(result1)