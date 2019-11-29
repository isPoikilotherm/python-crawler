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
html1 ='''
<ul class='list'>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
html2 ='''
<div class="wrap">
Hello,world!
<p>This is a paragraph.</p>
</div>
'''


from pyquery import PyQuery as pq
doc=pq(html)
doc_1=pq(html1)
doc_2=pq(html2)

#addClass和removeClass
li=doc('.item-0.active')
print(li)
li.remove_class('active')#从Class中删除active
print(li)
li.add_class('active')#向Class中添加active
print(li)

print('################################################################################################################################')

#attr\text和html
li_1=doc_1('.item-0.active')
print(li_1)
li_1.attr('name','link')#修改属性，参数为属性名和属性值
print(li_1)
li_1.text('yangliu')#节点内部的文本全部改为传入的字符串文本
print(li_1)
li_1.html('<span>yangliu</span>')#节点内部的文本全部改为传入的HTML文本
print(li_1)
#如果attr（）方法只传入第一个参数的属性名，则是获取这个属性值；如果传入第二个参数，可以用来修改属性值。
# text（）和html（）方法如果不传参数，则是获取节点内纯文本和HTML文本；如果传入参数，则进行赋值。

print('################################################################################################################################')

#remove()
wrap=doc_2('.wrap')
print(wrap.text())
print('**************************************************************')
wrap.find('p').remove()#删除p标签内容
print(wrap.text())