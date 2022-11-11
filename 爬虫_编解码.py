import urllib.request
url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
#请求对象定制
#将汉字转为unicode编码
import urllib.parse
name = urllib.parse.quote('周杰伦')
request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
