import requests,random

def get_one_page(url):
    proxies =[
        {'https': 'https://58.218.92.134:7494',
         'http': 'http://58.218.92.87:7915'},
        {'https': 'https://58.218.92.132:3902',
         'http': 'http://58.218.92.153:6188'},
        {'https': 'https://58.218.92.136:3576',
         'http': 'http://58.218.92.155:2157'},
        {'https': 'https://58.218.92.137:7451',
         'http': 'http://58.218.92.156:7833'},
        {'https': 'https://58.218.92.137:3955',
         'http': 'http://58.218.92.155:5123'},
        {'https': 'https://58.218.92.137:9566',
         'http': 'http://58.218.92.157:9533'},
        {'https': 'https://58.218.92.137:5513',
         'http': 'http://58.218.92.157:7608'},
        {'https': 'https://58.218.92.133:7980',
         'http': 'http://58.218.92.155:5571'}
    ]
    http=random.choice(proxies)
    headers = {
        'Cookie': 'uuid_n_v=v1; uuid=F440EBE009FE11EA805317C4792CDFD46B70F436C8DB4DED83F414498F9630F7; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1574080122,1574080156,1574138213; _lxsdk_cuid=16e7e7c8e9ec8-0a73d2081c873f-386b4644-1fa400-16e7e7c8e9ec8; _lxsdk=F440EBE009FE11EA805317C4792CDFD46B70F436C8DB4DED83F414498F9630F7; __mta=143382154.1574080122883.1574080433518.1574138226118.12; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=0b69cb9397b1b3bbb0abbbf1dc43c0922e5088883d437fdd8993071666ce3527; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1574138424; _lxsdk_s=16e82180bc7-eea-a1d-35%7C%7C1; lt=pjXdXSz_M3rjKlrV9QoJ1oaj318AAAAAawkAAMmaZqMiuwdPMWL_hkaE9c3jvrmtIe3o0Cfqz47INquj4okfvJ0CzvL1cTyweLbDjA; lt.sig=lqW_ftJHprWH8c0s7FvA8Phl43o',
        'Host': 'maoyan.com',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    rep=requests.get(url,headers=headers,verify=False)
    if rep.status_code ==200:
        return  rep.text
    return None