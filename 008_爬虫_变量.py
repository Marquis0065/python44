s='今天天气很好'
print(s *4)
'''
Number:int float
Boolean Ture False
String 字符串
List
Tuple 元组
Dictory 字典

'''
money = 5000 #int
money2 = 44.33 #float
#boolean 用于流程控制语句、性别
sex = True #用于表示性别男
sex = False #用于表示性别女
#字符串
string = '字符串'
print(string)
s2 = '"嵌套"'
print(s2)
s3 = '''双绰号'''
print(s3)
#list 应用场景，攫取图书类网站，所有图书接收
name_list = ['周杰伦','科比']
print(name_list)
#元组
age_tuple = (1,2,3,4,5)
print(age_tuple)
#dictory 应用于scrapy 框架 变量= ｛key:value}
person = {'name':'周敏','age':32}
# print(person)
# print(type(s3))
# print(type(person))
print(int('333'))
print(bool({}))
print(float('2.33'))
print(10//3)
print(10%3)
print(2**3)
a = b = 2
print(a)
print(b)
c, d, e = 1,3,4
print(e)
school = '中国人民大学'
sub = '临床医学'
print('我的学校是：%s; 专业是：%s'%(school,sub))
# # password = input('请输入密码：')
#
# print(password)
age = 9
if age>18:
    print('成年了')
else:
    print('还未成年')
s = 'china'
for  i in s:
    print(i)
print(type(range(1,5)))
a_list = ['a','b','c']
print(len(a_list))
for i in range(len(a_list)):
    print(a_list[i])
print(s.find('c'))#查找第一次出现的位置
print(s.startswith('a'))#判断是不是以某字母开头
print(s.endswith('c'))#c 以什么结尾
print(s.count('c'))
print(s.replace('c','a'))
print(a_list)
a_list.append('d')
print(a_list)
if 'd' in a_list:
    print('d存在于列表中')
del a_list[0]
print(a_list)
a_list.pop()
print(a_list)
a_list.remove('b')
print(a_list)
a_tuple = (1,2,3,4,5)
print(a_tuple)
print(type((2,)))

print({})
for i in a_tuple:
    print(i)
print(a_tuple[1])
dic = {'name':'fairy','age':23,'gender':'F'}
for key in dic.values():
    print(key)
for key,value in dic.items():
    print(key,value)
def f1():
    print('欢迎来到python世界')
    print("下次光临")

aa = 5
while aa>0:
    f1()
    aa -= 1

def sum(a,b):

    c = a + b
    print(c)
sum(11,22)



