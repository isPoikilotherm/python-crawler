import requests


# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,Value in r.cookies.items():
#     print(key+'='+Value)

headers={
    'Cookies':'_zap=2e24d036-6bf7-4532-9234-1d26699cfe46; _xsrf=988f754a-8d4d-4e76-adba-4f64ccc227d4; d_c0="AJDu1eGVWhCPTkwJpCf3otEfGqKKeGJRqWM=|1573736995"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1573736997,1573793086; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1573793086; tgw_l7_route=e5422eddfa4a8c2269da8eb93eb319b1; capsion_ticket="2|1:0|10:1573793072|14:capsion_ticket|44:MzI2YjU5N2M4ZGZiNDNjYjliMzdlMjU5MTZmOTkzY2Q=|0cde4d89bb38cc96386e893a31268434f31e68aacb8a2d3416d1a8dce15c40eb"; z_c0="2|1:0|10:1573793105|4:z_c0|92:Mi4xX2RGaUJBQUFBQUFBa083VjRaVmFFQ1lBQUFCZ0FsVk5VWHU3WGdCdF94TDljanhzZmRNU1R0dGk5R1plYy1ITFZ3|990c646a6d7d3e7d98274514bd0da8559f18d8da362ec3e7fe95a5463082a174"; unlock_ticket="ADBC5hC6dAsmAAAAYAJVTVk0zl37ZcFMQhKfyuHttuhIkfLqmFNNUQ=="; tst=r',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
r=requests.get('https://www.zhihu.com/people/liu-da-da-4-23/activities',headers=headers)
print(r.text)