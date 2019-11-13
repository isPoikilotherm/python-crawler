from urllib.parse import parse_qs

query = 'name=yangliu&age=23'
print(parse_qs(query))

#将一串GET请求参数转化为字典