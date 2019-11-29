html='''
<div class ="panel">
<div class ="panel-heading">
<h4>Hello</h4>
</div>element
<div class ="panel-body">
<ul class ="list" id="list-1">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
<li class ="element">Jay</li>
</ul>
<ul class ="list small" id="list-2">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
</ul>
</div>
</div>
'''

from bs4 import BeautifulSoup

soup=BeautifulSoup(html,'lxml')

#***************************************************************************
# print(soup.select('.panel .panel-heading'))#类名
# print(soup.select('ul li'))#节点名
# print(soup.select('#list-2 .element'))#id与class
# print(type(soup.select('ul')[0]))
# print(soup.select('ul')[0])
#***************************************************************************
#（1）嵌套选择
# for ul in soup.select('ul'):
#     print(ul.select('li'))
#***************************************************************************


#***************************************************************************
#（2）获取属性
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])
#***************************************************************************


#***************************************************************************
#（3）获取文本
for li in soup.select('li'):
    print('Get Text:',li.get_text())
    print('String:',li.string)