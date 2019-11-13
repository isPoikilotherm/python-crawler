from urllib import request,parse

url = 'https://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
#     'Host': 'httpbin.org'
# }
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))