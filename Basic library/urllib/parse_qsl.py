from urllib.parse import parse_qsl

query = 'name=yangliu&age=23'
print(parse_qsl(query))

#将一串GET请求参数转化为元组