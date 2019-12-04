from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')

#单个节点
input_1=browser.find_element_by_id('q')
input_1_1=browser.find_element(By.ID,'q')#通用方式
input_2=browser.find_element_by_css_selector('#q')
input_3=browser.find_element_by_xpath('//*[@id="q"]')
input_4=browser.find_element_by_class_name('search-combobox-input')
input_5=browser.find_element_by_name('q')
print(input_1,input_2,input_3,input_4,input_5)
browser.close()