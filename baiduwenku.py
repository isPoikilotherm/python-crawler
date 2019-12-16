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

https://wkbjcloudbos.bdimg.com/v1/docconvert2654//wk/de6004fb65191fea303b6557e28bf762/0.json?responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2030%20Jan%202020%2020%3A02%3A12%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-12-16T12%3A02%3A12Z%2F3600%2Fhost%2Fedcb31feb7afaf3cfebf6b11afc786fcc0815aafd6e802a9e53a4df3c0c9990f&x-bce-range=76359-91958&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjUwMTMzMiwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDYWNoZUNvbnRyb2wiLCJyZXNwb25zZUV4cGlyZXMiLCJ4LWJjZS1yYW5nZSJdfQ%3D%3D.jT0o46%2Bb%2F92vhf2ZxCuqzgnbfYiQucYzU3%2BwRnTlvP8%3D.1576501332

https://wkbjcloudbos.bdimg.com/v1/docconvert2654//wk/de6004fb65191fea303b6557e28bf762/0.json?responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2030%20Jan%202020%2020%3A02%3A12%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-12-16T12%3A02%3A12Z%2F3600%2Fhost%2Fedcb31feb7afaf3cfebf6b11afc786fcc0815aafd6e802a9e53a4df3c0c9990f&x-bce-range=91959-100235&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3NjUwMTMzMiwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDYWNoZUNvbnRyb2wiLCJyZXNwb25zZUV4cGlyZXMiLCJ4LWJjZS1yYW5nZSJdfQ%3D%3D.fdQIFPOBYDyLHqgUESnpTCIX65jpvQWq9PqHZtfpc28%3D.1576501332




# for li in lists:
#     print(li.text,end='')
# for li_1 in lists_1:
#     print(li_1.text,end='')
browser.close()


