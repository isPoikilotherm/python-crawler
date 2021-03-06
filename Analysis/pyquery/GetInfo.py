html ='''
<div class="wrap">
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
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

#获取节点属性
a=doc('.item-0.active a')#选中class为item-0和active的li节点内的a节点
print(a,type(a))
print(a.attr('href'))#调用attr（）方法，传入属性的名称，就可以得到属性值
print(a.attr.href)#得到a中href属性值
print('******************************************************************************')

a1=doc('a')
print(a1,type(a1))
print(a1.attr('href'))#当结果包含多个节点时，调用attr（）方法，只会得到第一个节点的属性
print(a1.attr.href)
for item in a1.items():
    print(item.attr('href'))#通过遍历得到每个a节点的属性

print('###############################################################################')
#获取文本
a3=doc('.item-0.active a')#选取一个a节点
print(a3)
print(a3.text())#调用text（）方法，忽略节点内部包含的所有HTML，只返回纯文字内容

print('******************************************************************************')
li=doc('.item-0.active')#选取第三个li节点
print(li)
print(li.html())#调用html（）方法，返回结果是li节点中的所有html文本

print('******************************************************************************')
li_1=doc('li')
print(li_1.html())#html()方法只返回第一个结果，若有多个结果，需要遍历
print(li_1.text())#text()方法以字符串类型返回所有结果的文本内容，无需遍历
print(type(li_1.text()))
