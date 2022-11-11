import requests
from lxml import etree
url = 'https://fs.lianjia.com/zufang/nanhai/pg3rt200600000001l1/#contentList'
response = requests.get(url)
response.encoding='utf8'
print(response.text)
print(response.url)
print(response.headers)
print(response.status_code)
tree = etree.HTML(response.text)
price_list = tree.xpath('//em/text()',encodings='utf8')
price_list.pop()
print(price_list)
