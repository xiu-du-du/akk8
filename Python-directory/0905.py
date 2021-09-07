#  选择结构
'''
year = 2020
# 单分支
if year > 2021:
    print("不是2021")

# 双分支
if year > 3030:
    print("未来")
else:
    print("现在")

# 多分支
if year < 1998:
    print("1")
elif year == 2000:
    print("2")
elif year >= 2020:
    print("3")
else:
    print("4")

# 多层选择结构的使用
day = 2020
moon = True
if day >= 2020:
    if moon:
        print('yes')
    else:
        print('no')
else:
    print("day not 2020!")

# 三目运算符
rs = '1' if day == 2020 else '2'
print(rs)
'''
# 作业一
'''
第一种:
if 条件语句:
    表达式
第二种:
if 条件语句:
    表达式
else:
    表达式
第三种:
if 条件语句:
    表达式
elif 条件语句:
    表达式
elif 条件语句:
    表达式
else:
    表达式
第四种:
if 条件语句:
    if 条件语句:
        表达式
    elif 条件语句:
        表达式
    else:
        表达式
else:
    表达式
第五种:
表达式 if 条件语句 else 表达式
'''

# 作业二
'''
x = input('输入x坐标：')
y = input('输入y坐标：')
if int(x) > 0:
    if int(y) > 0:
        print('你输入的坐标在第一象限')
    elif int(y) < 0:
        print('你输入的坐标在第四象限')
elif int(x) < 0:
    if int(y) > 0:
        print('你输入的坐标在第二象限')
    elif int(y) < 0:
        print('你输入的坐标在第三象限')
'''
# 作业三
'''
info = input('请输入分数：')
if int(info) >= 90:
    print('你的分数是：A')
elif 80 <= int(info) <= 89:
    print('你的分数是：B')
elif 70 <= int(info) <= 79:
    print('你的分数是：C')
elif 60 <= int(info) <= 69:
    print('你的分数是：D')
else:
    print('你的分数是：E')
'''
'''
a = 50
print(type(a))
b = 50
str(b)
print(type(b))
'''
# 循环结构
# while 循环
'''
a = 1
b = 0
while a <= 100:
    b += a
    a += 1
print(f'a的值是{a}，1~100的和是：{b}。')

# for 循环
for a in 'python':
    print(a)
for name in ['x', 't', 'z']:
    print(name)

# range(开始，结尾，步长) 默认从0开始
rs = 0
for i in range(1, 101):
    rs += i
print(f'a的值是{i}，1~100的和是：{rs}。')
'''
# 嵌套循环
''''
tmp = [
    ['1', '2', '3'],
    ['11', '22', '33'],
    ['111', '222', '333'],
    ['1111', '2222', '3333'],
]
'''
'''
i = 1
for count in tmp:
    print(f'周{i}观看指南：')
    for a in count:
        print(a)
'''
# range() 返回下标
'''
for a in range(len(tmp)):
    print(f'周{a+1}观看指南：')
    for name in tmp[a]:
        print(name)
'''


# enumerate() 返回下标和下标对应的值
'''
for a, count in enumerate(tmp):
    print(f'周{a+1}观看指南：')
    for name in count:
        print(name)
'''



# 作业一
i = 0
tmp1 = 0
# 累加和
while i < 101:
    tmp1 += i
    i += 1
print(tmp1)

a = 0
tmp2 = 0

# 偶数和
while a < 101:
    if a % 2 == 0:
        tmp2 += a
    a += 1
print(tmp2)

b = 0
tmp3 = 0
# 奇数和
while b < 101:
    if b % 2 == 1:
        tmp3 += b
    b += 1
print(tmp3)


# 作业二
i = 0
tmp1 = 0
# 累加和
for i in range(0, 101):
    tmp1 += i
    i += i
print(tmp1)

a = 0
tmp2 = 0
# 偶数和
for a in range(0, 101):
    if a % 2 == 0:
        tmp2 += a
    a += 1
print(tmp2)

b = 0
tmp3 = 0
# 奇数和
for b in range(0, 101):
    if b % 2 == 1:
        tmp3 += b
    b += 1
print(tmp3)

# 作业三
i = 0
a = 0
for i in range(5):
    for a in range(4):
        print(i, end=' ')
    print(i)


