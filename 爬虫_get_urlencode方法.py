import urllib.request
import urllib.parse
#用于多个请求方法
data = {
    'wd':'周杰伦',
    'sex':'男'
}
print(urllib.parse.urlencode(data))