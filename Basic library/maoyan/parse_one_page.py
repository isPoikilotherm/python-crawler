import re

def parse_one_page(html):

    pattern = re.compile('<div.*?cinema-cell.*?cinema-name.*?>(.*?)</a>.*?<p.*?cinema-address.*?>(,*?)</p>',re.S)
    items=re.search(pattern,html)
    print(items)
    # for item in items:
    #     print(item[1])

        # yield{
        #  'idex':item[0],
        #  'title':item[1].strip(),
        #  'star': item[2].strip(),
        #  'time': item[3].strip(),
        #  'score': item[4].strip()+item[5].strip()
        # }
