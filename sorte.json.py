import urllib.request
import urllib.parse
import jsonpath
from lxml  import etree
import json
obj = json.load(open('D:/DevInstall/Rtools/rtools40/store.json','r',encoding='utf8'))
import os
print(os.path.exists('D:/DevInstall/Rtools/rtools40/store.json'))
fp = open('store.json','r',encoding='utf8')
print(type(fp.read()))
print(type(obj))
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author_list)
print(jsonpath.jsonpath(obj,'$.store.*'))
print(jsonpath.jsonpath(obj,'$.store..price'))
print(jsonpath.jsonpath(obj,'$.store.book[3].title'))
print(jsonpath.jsonpath(obj,'$..book[(@.length-1)]'))

print(jsonpath.jsonpath(obj,'$..book[]'))
print('***********************')
print(jsonpath.jsonpath(obj,'$..book[?(@.price>10)]'))