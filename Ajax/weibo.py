from pyquery import PyQuery as pq
from pymongo import MongoClient
from urllib.parse import urlencode
import requests
base_url='https://m.weibo.cn/api/container/getIndex?'

headers={
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
def get_page(page):
    params={
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url=base_url + urlencode(params)
    try:
        respones=requests.get(url,headers=headers)
        if respones.status_code==200:
            return respones.json()
    except requests.ConnectionError as e:
        print('error',e.args)

def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item =item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text']=pq(item.get('text')).text()
            weibo['attitudes']=item.get('attitudes_count')
            weibo['comments']=item.get('comments_count')
            weibo['reposts']=item.get('reposts_count')
            yield weibo

if __name__ == '__main__':
    client=MongoClient(host='localhost',port=27017)
    db=client['weibo']
    collection=db.weibo
    for page in range(4,10):
        json=get_page(page)
        results=parse_page(json)
        for result in results:
            if collection.insert(result):
                print('Save to Mongo successful')
            print(result)