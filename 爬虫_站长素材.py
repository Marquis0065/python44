import urllib.request
import urllib.parse
from lxml import etree
#https://sc.chinaz.com/tupian/qinglvtupian_3.

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
for i in range(1,10):
    if i == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_'+str(i)+'.html'
    request = urllib.request.Request(url=url,headers=header)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    tree = etree.HTML(content)
    src_list = tree.xpath("//img[@class='lazy']/@data-original")
    name_list = tree.xpath("//img[@class='lazy']/@alt")
    for i in range(len(src_list)):
        name = name_list[i]
        src = 'https:'+src_list[i]
        urllib.request.urlretrieve(url=src,filename='./love_img/'+name+'.jpg')


