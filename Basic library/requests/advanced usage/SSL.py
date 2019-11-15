import requests
import urllib3

urllib3.disable_warnings()
r=requests.get('https://www.12306.cn',verify=False)
print(r.status_code)