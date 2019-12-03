from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input_1=browser.find_element_by_id('q')
input_2=browser.find_element_by_css_selector('#q')
input_3=browser.find_element_by_xpath('//*[@id="q"]')
input_4=browser.find_element_by_class_name('search-combobox-input')
input_5=browser.find_element_by_name('q')
print(input_1,input_2,input_3,input_4,input_5)
browser.close()