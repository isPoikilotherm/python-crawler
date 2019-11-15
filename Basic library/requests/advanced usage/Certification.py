import requests
from requests.auth import HTTPBasicAuth
from oauthlib import oauth1

#requests自带的身份认证
r=requests.get(url='',auth=HTTPBasicAuth('username','password'))
#上句中HTTPBasicAuth可以省略

#oauth1身份认证
url = 'https://api.twitter.com/1.1/account/verify_credential.json'
auth = oauth1('YOUR_APP_KEY','YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
r=requests.get(url,auth=auth)



print(r.status_code)