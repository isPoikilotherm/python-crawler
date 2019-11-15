import requests

data={
    'name':'yangliu',
    'age':'23'
}
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)