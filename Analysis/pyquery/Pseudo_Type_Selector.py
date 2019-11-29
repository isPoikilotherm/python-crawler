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

from pyquery import  PyQuery as pq
doc=pq(html)
li=doc('li:first-child')#选择第一个li节点
print(li)
li=doc('li:last-child')#选择最后一个li节点
print(li)
li=doc('li:nth-child(2)')#选择第二个li节点
print(li)
li=doc('li:gt(2)')#选择第三个li节点之后的li节点
print(li)
li=doc('li:nth-child(2n)')#选择偶数位置的li节点
print(li)
li=doc('li:contains(second)')##选择包含second文本的li节点
print(li)