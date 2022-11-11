import urllib.request
#1定义一个url
url = 'http://www.baidu.com'
#2模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# #3获取页面的原码，并解码
# content = response.read().decode('utf8')
# #4将二进制的数据转为字符串，解码
# print(content)
#一个类型六个方法
print(type(response))  #HTTPresponse类型
print(response.geturl())
print(response.getcode())
content = response.read(5)
content1 = response.readline()
print(content1)
content2 = response.readlines()
print(response.getheaders())#状态信息用户响应头


