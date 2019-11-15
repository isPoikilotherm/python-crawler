import  http.cookiejar,urllib.request

cookis = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookis)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for i in cookis:
    print(i.name+"="+i.value)