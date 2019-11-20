import requests
import re

proxies={
    # 'http':'http://47.107.172.6:8000',
    'https':'27.152.91.79:9999'
}

headers={
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding':'gzip,deflate,br',
    # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cookie':'partner=www_baidu_com; guid=7bb02c0c9fab0ee812eb99257fe7752d; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60050000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60050000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA40%2C32%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAWeb%C7%B0%B6%CB%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'Host':'mq.51job.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
r=requests.get('https://mq.51job.com/co1461258/',headers=headers)
r.encoding='gb2312'#解决中文不能正常显示

#r1=str(r)
#print(type(r))
#print(r.title())
results = re.findall('<strong.*?class="at".*?target="_blank".*?>(.*?)</a>',r.text,re.S)
#print(results)
for result in results:
    print(result)

