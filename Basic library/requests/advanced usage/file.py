import requests

files={'file':open('image.png','rb')}
r = requests.post('https://httpbin.org/post',files=files)
print(r.text)