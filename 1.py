import os

from bs4 import BeautifulSoup

html=open(os.path.join('/home/yangliu/Documents/WeChat Files/yangliu199610/FileStorage/File/2019-12/actionkit$0.html'),mode='r',encoding='utf-8').read()
soup=BeautifulSoup(html,'lxml')
api=soup.select_one('.inline.odd.last')
flow=soup.select('#followers .username')
#print(flow[2])
for f in flow:
    name=f.getText()
    print(api.text,name)

