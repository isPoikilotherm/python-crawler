html="""
<html>
<head>
<title> The Dormouse’s story</title>
</head>
<body>
<p class ="story"> 
Once upon a time there were three little sisters; and their names were
<a href ="http://example.com/elsie" class="sister" id ="link1">
<span>Elsie</span>
</a>
hello
<a href ="http://example.com/lacie" class ="sister" id ="link2">Lacie</a>
and
<a href="http://example.com/tillie" class ="sister" id ="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class ="story"> ... </p>
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')


#print(soup.p.contents)#输出p节点所有内容，每个元素都是p节点的直接子节点


# print(soup.p.children)#返回结果是生成器类型
# for i,child in enumerate(soup.p.children):
#     print(i,child)


# print(soup.p.descendants)#递归查询所有子节点，得到所有的子孙节点
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)


# print(soup.a.parent)#获取指定节点的直接父节点，没有再向外寻找祖先节点


# print(type(soup.a.parents))#（生成器类型）获取所有的祖先节点，以列表输出
# print(list(enumerate(soup.a.parents)))


# print('Next Sibling',soup.a.next_sibling)#获取下一个兄弟节点
# print('Prev Sibling',soup.a.previous_sibling)#获取上一个兄弟节点
# print('Next Siblings',list(enumerate(soup.a.next_siblings)))#获取后面所有的兄弟节点
# print('Prev Siblings',list(enumerate(soup.a.previous_siblings)))#获取前面所有的兄弟节点


print('Next Sibing:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)#下一个兄弟节点
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents))#所有祖先节点组成的列表
print(list(soup.a.parents)[0])#第一个父节点
print(list(soup.a.parents)[0].attrs['class'])#第一个父节点的class属性