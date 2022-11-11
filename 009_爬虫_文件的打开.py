open('test2.txt','w',encoding='utf8').write('天天')
fp = open('test.txt','r')
content = fp.read()
print(content)
print(type(content))
fp.close()
import json