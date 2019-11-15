from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)

#将内容转化为URL编码的格式