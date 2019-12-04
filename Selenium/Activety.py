from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input_1=browser.find_element_by_id('q')
# input_1.send_keys('iphone')
# time.sleep(3)
# input_1.clear()
input_1.send_keys('加湿器')
but=browser.find_element_by_css_selector('.btn-search.tb-bg')
but.click()