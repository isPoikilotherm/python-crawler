from urllib.parse import urljoin

print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://yangliu.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://yangliu.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://yangliu.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc','https://yangliu.com/index.php'))
print(urljoin('http://www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com#comment','?category=2'))
# base_url提供了三项内容scheme，netloc和path。如果这3项在新的链接里不存在，就予以补充；如果新的链接在，就使用新的链接的
# 部分。而base_url中的params、query和fragment是不起作用的。