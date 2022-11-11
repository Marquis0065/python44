import urllib.request
import urllib.parse
import urllib.error

url = 'https://movie.douban.com/j/chart/top_list?type=1&interval_id=100%3A90&action=&start=0&limit=20'
header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

}
request = urllib.request.Request(url=url ,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
fp = open('douban.json','w',encoding='utf8')
fp.write(content)


