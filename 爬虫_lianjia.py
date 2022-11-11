import urllib.request
import urllib.parse
from lxml import etree
import json
base_url = 'https://fs.lianjia.com/zufang/chancheng/pg'
# response = urllib.request.urlopen(base_url)
# content = response.read().decode('utf8')
for i in range(1,42):
    url = base_url+str(i)+'rt200600000001l1/#contentList'
    content = urllib.request.urlopen(url).read().decode('utf8')
    tree = etree.HTML(content)
    result = tree.xpath('///em/text()')
    print(result)
    with open('price2.txt','a',encoding='utf8')as fp:
        fp.write(json.dumps(result)+'\n')



