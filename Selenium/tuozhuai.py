from selenium import webdriver
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')#转化到frame窗口中
start=browser.find_element_by_id('draggable')
end=browser.find_element_by_id('droppable')
actions=ActionChains(browser)
actions.drag_and_drop(start,end)#确定位置
actions.perform()#执行动作