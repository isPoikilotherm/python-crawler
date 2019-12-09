from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')#进入id为iframeResult的子frame（子页面）
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No Have!')
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print('logo')
print(logo.text)