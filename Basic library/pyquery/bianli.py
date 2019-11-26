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

from pyquery import PyQuery as pq
doc=pq(html)
li=doc('.item-0.active')
print(li)#直接打印输出
print(str(li))#转换为字符串后输出

lis=doc('li').items()#调用items方法得到一个生成器
print(type(lis))
for li1 in lis:
    print(li1,type(li1))#遍历逐个得到li节点对象