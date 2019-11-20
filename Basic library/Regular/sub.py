import re

content = '57y45an545g4548li0245u4454'
content=re.sub('\d+','',content)
print(content)
#替换某种元素