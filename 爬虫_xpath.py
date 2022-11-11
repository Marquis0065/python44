import urllib.request
import urllib.parse
from lxml import etree
url = 'http://www.baidu.com'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url = url ,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
# print(content)
tree = etree.HTML(content)
result = tree.xpath("//input[@id='su']/@value")[0]
print(result)
