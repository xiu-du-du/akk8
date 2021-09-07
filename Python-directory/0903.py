# 数据类型的使用
# 数值型
int1 = 10
float1 = 10.2
# 字符串str
str1 = 'allen'
# 布尔值bool
bool1 = True
bool2 = False
# type()查看数据类型的方法
print(type(int1))
print(type(float1))
print(type(str1))
print(type(bool1))
print(type(bool2))

# 容器
# 列表list
list1 = [10, 20, 30]
# 元组tuple
tuple1 = (100, 200, 300)
# 集合set
set1 = {101, 202, 303}
# 字典dict
dict1 = {"name": "allen"}

print(list1)
print(tuple1)
print(set1)
print(dict1)

print(type(list1))
print(type(tuple1))
print(type(set1))
print(type(dict1))

# 复制运算符的使用
name = 'Tom'
print(name)
# 这种写法左右的值要相等
num1, num2, num3 = 10, 30, 50
print(num1, num2, num3)

a = b = c = 100
print(a, b, c)

'''
+= -= *= ....
'''
a = b = c = 200
a += 100
# b=b*(3+2)
b *= 3 + 2
print(a)
print(b)

# 比较运算符的使用
a = 100
b = 200
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

# 逻辑运算符的使用
# and-和 or-或 not-取反
a = 1
b = 2
c = 3

print("and 返回结果")
print(a > b > c)
print(a > b < c)
print(a < b < c)
print("or 返回结果")
print(a > b or b > c)
print(a > b or b < c)
print(a < b or b < c)
print("not 返回结果")
print(not a > b)
print(not a > c)
print(not b > c)

# 字符串创建
# 三个单引号或者三个双引号的字符串可以换行
name1 = 'Jerry'
name2 = "Tom"
name3 = '''
你好！
今天周五！
明天周六！
...
'''
name4 = """
你好！
今天周五！
明天周六！
...
"""
print(name1)
print(name2)
print(name3)
print(name4)

say = 'i\'m allen'
print(say)

# 输入操作
# uname = input("请输入账户名：")
# passwd = input("请输入密码：")
# print("你输入的用户名是：{0}, 密码是{1}。", uname, passwd)

# 输出
nameId = 'allen'
print(nameId)
print("我的名字是：", nameId)
print("我的名字是：{}".format(nameId))
print("我的名字是：{0}，{1}".format(nameId, "Hello"))
print("我的名字是：{n}".format(n=nameId))
print("我的名字是：%s" % nameId)
print(f"我的名字是：{nameId}")     # 常用方式

# 字符串下标的使用
info = '我1有2一个大钱包！'
print(info[0])
print(info[-1])
print(info[0:1])
print(info[:-3])
print(info[-3:])
print(info[:3])
print(info[3:])
print(info[3:6])
print(info[::-1])   # 开始：结束：步长   负数就是将文本倒过来输出
print(info[::2])

# 字符串常用的方法
# 查找 判断 修改
info = 'hello python and world and allen'
# find index count
print("="*10, 'find', '='*10)
print(info.find('and'))
print(info.find('and', 15, 30))
print("="*10, 'index', '='*10)
# index 返回下标，没有找到字符串就会报错
print(info.index('and'))
print(info.index('and', 15, 30))
print("="*10, 'count', '='*10)
# count 找到字符串在文本中有几处
print(info.count('and'))
print(info.count('and', 15, 30))

print("="*10, '字母大小写操作', '='*10)
print(info.upper())  # 字符串全部文本大写
print(info.lower())  # 字符串全部文本小写
print(info.title())  # 字符串中每个单词的首字母大写
print(info.capitalize())  # 字符串中第一个字母大写

print("="*10, '字符串替换', '='*10)
# replace(要替换的文本，替换的文本，替换的次数) 字符串替换
print(info.replace("and", "or"))
print(info.replace("and", "or", 1))

print("="*10, '字符串分割', '='*10)
# split(分割符) 字符串分割
temp = info.split("and")
print(temp)
temp = info.split(" ")  # 分割
print(temp)

print("="*10, '字符串拼接', '='*10)
# join(多字符串组成的序列) 字符串替换
a = "@拼接符@"
print("join:", a.join(temp))  # 拼接

# 去除字符串的空格
info2 = '    hello  world !    '
print(info2.strip())   # 去除两端空格
print(info2.lstrip())   # 去除左边空格
print(info2.rstrip())   # 去除右边空格
print("="*10, '判断是否是指定的字符', '='*10)

# startswith endswith 判断是否是指定字符
print(info2.startswith("hello", 4, 25))
print(info.startswith("hello"))
print(info.endswith("and"))
print(info.endswith("allen"))
print("="*10, '判断是否是指定类型的字符串', '='*10)

# isdigit() isalpha() isalnum() 判断是否是指定类型的字符串
info3 = '123'
info4 = 'wasd'
info5 = 'asd123'
info6 = '   w'

print(info3.isdigit())  # 数字
print(info4.isalpha())  # 字母
print(info5.isalnum())  # 数字或字母
print(info6.isspace())  # 空白

print('='*10 + '课程作业' + '='*10)
'''
【课程作业】
1、使用字符串复制：用技术安吉打印“爱你一百遍”，打印100次
2、将“to be or not to be”字符串倒序输出
3、将“ChinaChinaChina”字符串中所有的c输出
'''
# 作业一：
print("爱你一百遍\n"*100)
# 作业二：
info7 = 'to be or not to be'
print(info7[::-1])
# 作业三：
info8 = 'ChinaChinaChina'
print(info8[::5])
