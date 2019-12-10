import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')#调用execute_script方法，传入window.open()这个JavaScript语句新开启一个选项卡
print(browser.window_handles)#获取当前所有的选项卡，返回选项卡的代号序列
browser.switch_to_window(browser.window_handles[1])#switch_to_window（）跳转选项卡，参数为选项卡代号
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.python.org')