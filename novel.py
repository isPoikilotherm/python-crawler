import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

def getpage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    html = requests.get(url, headers=headers)
    html.encoding='utf-8'
    doc = pq(html.text)
    name=doc('.bookname h1').text()
    content=doc('#content').text()
    file = open('都市虫皇.txt', 'a', encoding='utf-8')
    file.write('\n'+name+'\n')
    file.write('\n'+content+'\n')
    file.close()

if __name__ == '__main__':
    num=299318
    while 1:
        if num < 299484:
            getpage('http://www.biquge.info/0_619/' + str(num) + '.html')
            num = num + 1
        else:
            num_1 = 3282412
            if num_1 < 3282703:
                getpage('http://www.biquge.info/0_619/' + str(num_1) + '.html')
                num_1 = num_1 + 1
            else:
                break

