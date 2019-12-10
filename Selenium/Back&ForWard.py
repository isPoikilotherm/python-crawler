import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()  # 返回第二个页面
time.sleep(1)
browser.forward()  # 前进到第三个页面
browser.close()
