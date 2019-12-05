from selenium import webdriver
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
logo=browser.find_element_by_id('Popover1-toggle')
print(logo)
print(logo.get_attribute('class'))
print(logo.get_attribute('placeholder'))


