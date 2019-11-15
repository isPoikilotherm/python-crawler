import requests

s=requests.Session()
s.get('http://www.httpbin.org/cookies/set/number/123456789')
r=s.get('http://www.httpbin.org/cookies')
print(r.text)