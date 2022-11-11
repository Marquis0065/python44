import urllib.request

url = 'https://www.baidu.com'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# rsponse = urllib.request.urlopen(url)
# content = rsponse.read().decode('utf8')
# print(content)
#请求对象的定制，urlopen方法中不能存储字典，header不能传入
#定制
request = urllib.request.Request(url=url,headers=header)
content = urllib.request.urlopen(request).read().decode('utf8')
print(content)

