import requests

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
r=requests.get('http://www.jianshu.com',headers=headers)
print(r.status_code)
exit() if not r.status_code==requests.codes.ok else print('successfully')
#通过比较返回码和内置的成功的返回码，来保证请求得到了正常的响应