from selenium import webdriver
import time

browser=webdriver.Chrome()
url='https://wenku.baidu.com/view/e1e1adbef121dd36a32d82c3.html?rec_flag=default&sxts=1576496681535'
browser.get(url)
# lists=browser.find_elements_by_css_selector('.ie-fix p')
js='document.getElementsByClassName("down-arrow goBtn")[0].click();'
browser.execute_script(js)
lists_1=browser.find_element_by_id('pageNo-12')
print(browser.page_source)
#li=lists_1.find_element_by_css_selector()





# for li in lists:
#     print(li.text,end='')
# for li_1 in lists_1:
#     print(li_1.text,end='')
browser.close()


