from urllib.parse import urlencode

params = {
    'name':'yangliu',
    'age':'23'
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
#从字典转化为GET请求中的URL参数