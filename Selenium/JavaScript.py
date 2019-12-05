from selenium import webdriver


browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滑轮到页面底部
browser.execute_script('alert("To Bottom")')