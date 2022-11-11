import requests
from lxml import etree

url = 'https://www.apple.com.cn/iphone/'
response = requests.get(url)
print(response)
tree = etree.HTML(response.text)
result = tree.xpath("//a[@class='chapternav-link']/span[1]/text()")
print(result)