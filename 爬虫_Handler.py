import urllib.request
url = 'http://www.baudu.com'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url ,headers=header)

#获致Handler对象
handler = urllib.request.HTTPHandler()
#获取opener对象
opener = urllib.request.build_opener(handler)
#调用opener方法
response = opener.open(request)
content = response.read().decode('utf8')
print(content)