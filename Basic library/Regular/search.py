import requests
import re


headers={
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding':'gzip,deflate,br',
    # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cookie':'x-zp-client-id=2fcd685f-f39d-4811-9305-6f31cbe4e184; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e7944e52271e-0b93478836b76b-386b4644-2073600-16e7944e523971%22%2C%22%24device_id%22%3A%2216e7944e52271e-0b93478836b76b-386b4644-2073600-16e7944e523971%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; sajssdk_2015_cross_new_user=1; sts_deviceid=16e7945678f635-0409748e1b294d8-386b4644-2073600-16e79456790e0a; dywea=95841923.1466944816545315600.1573992622.1573992622.1573992622.1; dyweb=95841923.1.10.1573992622; dywec=95841923; dywez=95841923.1573992622.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1573992622; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573992635; sts_sg=1; sts_evtseq=4; sts_sid=16e7945697a525-02910bf4e62a1-386b4644-2073600-16e7945697b33f; sts_chnlsid=Unknown; jobRiskWarning=true; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; __utma=269921210.556966954.1573992623.1573992623.1573992623.1; __utmb=269921210.1.10.1573992623; __utmc=269921210; __utmz=269921210.1573992623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; acw_tc=3da2311615739926309855880e8b1ecd5527c5396e0fbb5691695eb45e; acw_sc__v2=5dd138b7b9aaec12090ff345d07728913ce780c3; sou_experiment=unexperiment; FSSBBIl1UgzbN7N443S=WuBtnCToqHjJeFz3A1mtTHuK7KD943222oi9CjGRF5EYvJ79LTcEUsaKL8U36U1d; FSSBBIl1UgzbN7N443T=4rj_iPwaEYDQWs1O4WUZiL9KNycE3Fgwi66HWU4VgYKDXo8n6BeuJ00uOaVSTMLgLZP9u1cRKDl9wFBJDZsIaoWUXmFxmxXLrPSckJXShl80rr7RNPDdwJV7B7sD7HSDnU42FJwGYxWyvi0_Zfx3F1JOP_ZhQy3vRyFaKpRWLvyM6rf8Ogg7.rJpPQSivVjulYRp_FHm1MPTmANFXbYEkqcbTa_heCBogT9UMNwt6WfoOZa; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22bd288435-6cdb-4aab-8d96-29558550f5c3-sou%22%2C%22funczone%22:%22smart_matching%22}}; LastCity=%E5%A4%A9%E6%B4%A5; LastCity%5Fid=531; ZP_OLD_FLAG=false; POSSPORTLOGIN=8; CANCELALL=1; zp_src_url=https%3A%2F%2Fwww.zhaopin.com%2F',
    'Host':'sou.zhaopin.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
r=requests.get('https://sou.zhaopin.com/?jl=531&kw=Java%E5%BC%80%E5%8F%91&kt=3',headers=headers)
print(r.text)
#print(type(r))
#r1=str(r)
#print(type(r))
#print(r.title())
result = re.search('<a.*?query-industry__uls__item__name.*?>(.*?)</a>',r.text,re.S)
print(result.group(1))