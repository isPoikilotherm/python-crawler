html ='''
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html1 ='''
<div class="wrap">
<div id='container'>
<ul class='list'>
<li class="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

from pyquery import PyQuery as pq
doc=pq(html)
doc1=pq(html1)
# #基本CSS选择器
# print(doc('#container .list li'))
# #选取id为container的节点（#表示选取id），再选取其内部的class为list的节点内部的所有li节点（。表示选取class）
# print(type(doc('#container .list li')))


# #查找子节点
# items=doc('.list')#选取class为list的节点内容
# print(type(items))
# print(items)
# lis=items.find('li')#find（）方法选取item中的所有li节点（find方法查找的范围是节点的所有子孙节点）
# print(type(lis))
# print(lis)
# lis1=items.children()#只查找item的子节点，不查找孙节点
# print(type(lis1))
# print(lis1)
# lis2=items.children('.active')#只查找item的class为active的子节点
# print(lis2)


# #查找父节点
# items=doc1('.list')
# container=items.parent()#得到item的直接父节点，不会查找祖先节点
# print(type(container))
# print(container)
#
# parents=items.parents()#得到item的所有祖先节点
# print(type(parents))
# print(parents)
#
# parents=items.parents('.wrap')#得到item的class为wrap的祖先节点
# print(parents)


#查找兄弟节点
li=doc('.list .item-0.active')#选择class为list的节点内部class为item-0和active的节点（第三个li节点）
print(li.siblings())#查找li的所有兄弟节点

li1=doc('.list .item-0.active')#选择class为list的节点内部class为item-0和active的节点（第三个li节点）
print(li1.siblings('.active'))#查找li1中的class为active的兄弟节点