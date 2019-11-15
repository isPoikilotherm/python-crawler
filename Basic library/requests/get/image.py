import requests

r=requests.get('https://github.com/favicon.ico')
with open('favicon1,ico','wb') as f:
    f.write(r.content)
# print(r.text)
# print(r.content)