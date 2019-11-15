import requests

proxies={
    # 'http':'http://47.107.172.6:8000',
    'https':'https://47.106.231.64:3128'
}
r=requests.get('https://www.taobao.com',proxies=proxies)
print(r.text)