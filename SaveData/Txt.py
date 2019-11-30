import requests
from pyquery import PyQuery as pq

url='https://www.lagou.com/zhaopin/Java/?labelWords=label'
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Cookie':'user_trace_token=20191129133532-e3137daf-1432-4d46-877e-2ee179bff80a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575005734,1575005745; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1575006008; _ga=GA1.2.2051592528.1575005734; _gat=1; LGSID=20191129133545-17458644-126a-11ea-a68e-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0oWuh0FNkUs06o8KI00000nMYN-C00000UlKAzM.THL0oUhY1x60UWdVUv4_py4-g1PxuAT0T1dhuhR1ujnvuj0snj0sPhm30ZRqPWRLnjIKfbPawRm1wbNjwWnkPDcLnHc4nWNawjuKf1R0mHdL5iuVmv-b5Hn1nHR3nWmsP1bhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5Hf4rj6Y%26tpl%3Dtpl_11534_21150_17267%26l%3D1515648201%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3315826079_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D194%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGRID=20191129134008-b3fafc15-126a-11ea-aa15-525400f775ce; LGUID=20191129133533-10523138-126a-11ea-a68e-5254005c3644; X_HTTP_TOKEN=bb7777aff58a6d878006005751ddea52048f251e9a; gate_login_token=b18addce5a70b78db01238e6f0366eb12cd3c4f4bc7826c227eda770e270da45; LG_HAS_LOGIN=1; _putrc=9E6BBDCDE241F1FD123F89F2B170EADC; JSESSIONID=ABAAABAAAIAACBIA914816C220F7F10E8BD0680E94B6AC9; login=true; unick=%E6%9D%A8%E6%9F%B3; hasDeliver=0; privacyPolicyPopup=false; _gid=GA1.2.1201057225.1575005792; WEBTJ-ID=20191129133950-16eb5ac2e8e448-0d832b79fcd6a8-386b4644-2073600-16eb5ac2e8f8c9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216eb5ac2f42ace-0c3e27e21dd3ad8-386b4644-2073600-16eb5ac2f433ec%22%2C%22%24device_id%22%3A%2216eb5ac2f42ace-0c3e27e21dd3ad8-386b4644-2073600-16eb5ac2f433ec%22%7D; sajssdk_2015_cross_new_user=1; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_navigation; SEARCH_ID=efda334cd0e847a788d47da205fa69dc'
}
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.con_list_item.default_list').items()
for item in items:
    position=item.find('h3').text()
    place=item.find('.add').text()
    company=item.find('.company_name').text()
    money=item.find('.money').text()
    qualification=item.find('.p_bot').text()
    industry=item.find('.industry').text()
    detail=item.find('.list_item_bot').text()
    file=open('zhaopin1.txt','a',encoding='utf-8')
    file.write('\n'.join([position,place,company,qualification,industry,detail]))
    file.write('\n'+'='*50+'\n')
    file.close()