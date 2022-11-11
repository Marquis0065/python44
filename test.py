import urllib.request
import urllib.parse
from lxml import etree
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'

requets = urllib.request.Request(url = url ,headers=header)
response = urllib.request.urlopen(requets)
content = response.read().decode('utf8')
tree = etree.HTML(content)
result = tree.xpath("//img[@class='lazy']/@src")
print(len(result))