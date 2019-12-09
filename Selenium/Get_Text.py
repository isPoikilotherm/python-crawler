from selenium import webdriver

browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
bton=browser.find_element_by_css_selector('.Button.Button--primary.Button--blue')
print(bton.text)#获取文本
print(bton.id)#获取id
print(bton.location)#获取相对位置
print(bton.tag_name)#获取标签名称
print(bton.size)#获取节点大小
