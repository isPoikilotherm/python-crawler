import datetime
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By



class YuYue():
    def __init__(self):

        #self.browser.implicitly_wait(time_to_wait=10)
        self.domain='http://ligong.deshineng.com:8082/brmclg/index.html?v=1'


    def get(self):
        starttime=datetime.datetime(2020,6,16,6,0,10)
        #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        while True:
            currenttime = datetime.datetime.now()
            if currenttime>starttime:
                chrome_options = Options()
                # 设置chrome浏览器无界面模式
                chrome_options.add_argument('--headless')
                self.browser = webdriver.Chrome(chrome_options=chrome_options)
                self.browser.get(self.domain)
                time.sleep(1)
                self.browser.find_element_by_id('code').send_keys("193131315")
                self.browser.find_element_by_id('passwd').send_keys("199610")
                self.browser.find_element_by_name('agreecheck').click()
                self.browser.find_element_by_id('login-button').click()
                time.sleep(1)
                self.browser.find_element_by_xpath('//*[@id="example-navbar-collapse"]/ul/li[1]/a').click()
                self.browser.find_element_by_xpath('//*[@id="category_A"]/li[2]/a').click()
                time.sleep(2)
                tijiao = self.browser.find_element_by_xpath('//*[@id="book-status-list"]/tbody/tr[45]/td[2]/button')
                # tijiao=self.browser.find_element_by_partial_link_text('进入时间:22:00-22:10')
                self.browser.execute_script("arguments[0].click()", tijiao)
                time.sleep(1)
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                self.browser.close()
            # else:
            #     print("时间未到")


if __name__ == '__main__':
    yuyue=YuYue()
    yuyue.get()






















