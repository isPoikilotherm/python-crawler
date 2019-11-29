html='''
<div class ="panel">
<div class ="panel-heading">
<h4>Hello</h4>
</div>
<div class ="panel-body">
<ul class ="list" id="list-1">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
<li class ="elernent">Jay</li>
</ul>
<ul class ="list list-small" id＝"list-2">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
</ul>
</div>
</div>
'''
html1='''
<div class ="panel">
<div class ="panel-heading">
<h4>Hello</h4>
</div>
<div class ="panel-body">
<ul class ="list" id="list-1" name="element">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
<li class ="elernent">Jay</li>
</ul>
<ul class ="list list-small" id＝"list-2">
<li class ="element">Foo</li>
<li class ="element">Bar</li>
</ul>
</div>
</div>
'''
html2='''
<div class ="panel">
<div class ="panel-heading">
<h4>Hello</h4>
</div>
<div class ="panel-body">
<a>Hello,this is a link</a>
<a>Hello,this is a link,too</a>
</div>
</div>
'''
from bs4 import BeautifulSoup
import re

#**************************************************************************************
# #（1）name  根据节点名查询
# soup=BeautifulSoup(html,'lxml')
# print(soup.find_all(name='ul'))#查询所有ul节点，返回列表类型
# print(type(soup.find_all(name='ul')[0]))#每个元素都是bs4.element.Tag类型
#
#
##嵌套查找ul中的li节点
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))#嵌套查找ul中的li节点
#
#
##遍历每个li，得到文本
# for ul in soup.find_all(name='ul'):
#     for li in ul.find_all(name='li'):
#         print(li.string)#遍历每个li，得到文本
#**************************************************************************************


#**************************************************************************************
#（2）attrs  根据属性查询
# soup1=BeautifulSoup(html1,'lxml')

# #使用attrs传递
# print(soup1.find_all(attrs={'id':'list-1'}))#根据id属性查找，参数是字典类型
# print(soup1.find_all(attrs={'name':'element'}))#根据name属性查找


# #直接传递属性，适用id,class等常用属性
# print(soup1.find_all(id='list-1'))#根据id属性查找
# print(soup1.find_all(class_='element'))#class为关键字，要加下划线
#**************************************************************************************


#**************************************************************************************
#（3）text  用来匹配节点的文本，传入字符串或者正则对象
soup2=BeautifulSoup(html2,'lxml')
print(soup2.find_all(text=re.compile('link')))
#**************************************************************************************