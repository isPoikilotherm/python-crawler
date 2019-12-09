from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# #隐式等待
# browser=webdriver.Chrome()
# browser.implicitly_wait(time_to_wait=10)
# browser.get('https://www.zhihu.com/explore')
# bton=browser.find_element_by_css_selector('.Button.Button--primary.Button--blue')
# print(bton)


#显式等待
browser=webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait=WebDriverWait(browser,10)#指定最长等待时间
input=wait.until(EC.presence_of_element_located((By.ID,'q')))#传入要等待条件（presence_of_element_located）
#在10秒内如果Id为q的节点加载出来，就返回该节点，如果超过10秒还没有加载出来，就抛出异常
bton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))#以是否可点击作为条件
print(input,bton)