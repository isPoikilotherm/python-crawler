import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

r1=requests.get('http://www.httpbin.org/get')
print(type(r1.text))
print(r1.json())
print(type(r1.json()))#调用json方法，将返回结果是JSON格式的字符串转化为字典，如果不是JASON格式的，解析出错

# data={
#     'name':'yangliu',
#     'age':'23'
# }
# r2=requests.get('http://www.httpbin.org/get',params=data)
# print(r2.text)