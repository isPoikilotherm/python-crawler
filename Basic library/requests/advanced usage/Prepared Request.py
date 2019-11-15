from  requests import Request,Session

url='http://httpbin.org/post'
data={
    'name':'yangliu'
}
headers={
     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
s=Session()

#用URL，data和headers参数构造了一个Request对象
req=Request('POST',url,data=data,headers=headers)

#调用Session的prepare_request（）方法将其转换为一个Prepare Request对象
prepped=s.prepare_request(req)

#调用send方法发送
r=s.send(prepped)
print(r.text)