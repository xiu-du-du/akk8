# 0903-数据类型和字符串操作
>编写python程序的文件，称为python的脚本或程序。
>要求当前python文件的后缀名必须是.py

#### Python中的注释

>注释就是一段说明文字，不会被执行。
> 在python的脚本中，开头的第一个字符如果是#号，那么就是注释了。
>''' 或者 “”“ 也是注释
## 基本数据类型

#### 变量

> 变量名=变量值
>
> 例如：a=321
>
> 变量名 命名规则：
>
> 1、由数字、字母、下划线组成
>
> 2、不能数字开头
>
> 3、不能使用内置关键字  //关键字就是系统占用了的标识字符
>
> 4、严格区分大小写

#### 标识符

|     and      |    as    |  assert   |   break    |    class     |    True    |
| :----------: | :------: | :-------: | :--------: | :----------: | :--------: |
| **continue** | **def**  |  **del**  |  **elif**  |   **else**   | **except** |
| **finally**  | **for**  | **from**  | **False**  |  **global**  |   **if**   |
|  **import**  |  **in**  |  **is**   | **lambda** | **nonlocal** |  **not**   |
|   **None**   |  **or**  | **pass**  | **raise**  |  **return**  |  **try**   |
|  **while**   | **with** | **yield** |            |              |            |

#### 命名习惯

> 1.见名知意
> 2.大驼峰：即每个单词首字母都大写。 例如：MyName
> 3.小驼峰：第二个开始以后的单词首字母都大写。例如：myName
> 4.下划线：例如：my_name

#### 数据类型

- dict 字典
- set 集合
- tuple 元组
- list 列表
- 数值
  - int 整数
  - float 浮点数
- bool 布尔值
- str 字符串

#### 运算符

| 运算符 |      描述      |               实例                |
| :----: | :------------: | :-------------------------------: |
|   =    |      赋值      | 将=右侧的结果赋值给等号左侧的变量 |
|   +=   | 加法赋值运算符 |         c+=a 等价于 c=c+a         |
|   -=   | 减法赋值运算符 |         c-=a 等价于 c=c-a         |
|   *=   | 乘法赋值运算符 |         c×=a 等价于 c=c×a         |
|   /=   | 除法赋值运算符 |         c/=a 等价于 c=c/a         |
|  //=   | 整除赋值运算符 |        c//=a 等价于 c=c//a        |
|   %=   | 取余赋值运算符 |         c%=a 等价于 c=c%a         |
|  **=   |  幂赋值运算符  |        c××=a 等价于 c=c××a        |

#### 比较运算符

| 运算符 |       描述       | 实例 |
| :----: | :--------------: | :--: |
|   =    |     判断相等     | a==b |
|   !=   |      不等于      | a!=b |
|   >    |   左侧大于右侧   | a>b  |
|   <    |   左侧小于右侧   | a<b  |
|   >=   | 左侧大于等于右侧 | a>=b |
|   <=   | 左侧小于等于右侧 | a<=b |

#### 逻辑运算符

| 运算符 | 逻辑表达式 | 描述 |                    实例                    |
| :----: | :--------: | :--: | :----------------------------------------: |
|  and   |  x and y   |  与  |          True and False,返回False          |
|   or   |   x or y   |  或  |           True or False,返回True           |
|  not   |   not x    |  非  | not True,返回False<br />not False,返回True |

## 字符串的使用

#### 字符串

````python
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
# 三个单引号或者三个双引号的字符串可以换行
````

````python
say = 'i\'m allen'
print(say)
# 斜杠代表转义字符，因此输出结果是:i'm allen
````

````python
# 输入操作
uname = input("请输入账户名：")
passwd = input("请输入密码：")
print("你输入的用户名是：{0}, 密码是{1}。", uname, passwd)

# input 会把接收到的任何数据当做字符串处理！！！
````

#### 输出

````python
# 输出
nameId = 'allen'
print(nameId)
print("我的名字是：", nameId)
print("我的名字是：{}".format(nameId))
print("我的名字是：{0}，{1}".format(nameId, "Hello"))
print("我的名字是：{n}".format(n=nameId))
print("我的名字是：%s" % nameId)
print(f"我的名字是：{nameId}")     # 常用方式
````

#### 下标

> 字符串、列表、元组都支持切片操作

````python
# 字符串下标的使用
info = '我有一个大钱包'
print(info[0])
print(info[-1])
# 负数代表从后开始取，正数代表从前开始取
````

````python
info = '我1有2一个大钱包，里面装有很多钱！'
print(info[0])
print(info[-1])
print(info[0:1])
print(info[:-3])
print(info[-3:])
print(info[:3])
print(info[3:])
print(info[3:6])
print(info[::-1])   # 3个冒号代表 开始：结束：步长   负数就是将文本倒过来输出
print(info[::2])  # 字符串内容直接的步长间隔为1，设置步长为2就可以跳过一个输出
# info[0:3] 开始的下标包含，结束的下标不包含!!!
````

#### 字符串常用的方法

````python
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
# 输出结果：
'''
========== 字母大小写操作 ==========
HELLO PYTHON AND WORLD AND ALLEN
hello python and world and allen
Hello Python And World And Allen
Hello python and world and allen
'''

# replace(要替换的文本，替换的文本，替换的次数) 字符串替换
print(info.replace("and", "or"))
print(info.replace("and", "or", 1))
print("="*10, '字符串分割', '='*10)

# split(分割符) 字符串分割
temp = info.split("and")
print(temp)
temp = info.split(" ")  # 分割
print(temp)
print("="*10, '字符串替换', '='*10)

# join(拼接符，字符串列表list) 字符串替换
print('    '.join(temp))  # 拼接
print("="*10, '去除字符串的空格', '='*10)

# 去除字符串的空格
info2 = '    hello  world !    '
print(info2.strip())   # 去除两端空格
print(info2.lstrip())   # 去除左边空格
print(info2.rstrip())   # 去除右边空格
print("="*10, '判断字符串首尾是否是指定字符', '='*10)

# startswith endswith 判断字符串首尾是否是指定字符
print(info.startswith("and"))
print(info.startswith("hello"))
print(info.endswith("and"))
print(info.endswith("allen"))
print("="*10, '判断是否是指定类型的字符串', '='*10)

# isdigit() isalpha() isalnum() 判断是否是指定类型的字符串
info3 = '123'
info4 = 'wasd'
info5 = 'asd123'
print(info3.isdigit())  # 数字
print(info4.isalpha())  # 字母
print(info5.isalnum())  # 数字或字母
print(info6.isspace())  # 空白
````

### 总结：

|              方法名               |                             作用                             |
| :-------------------------------: | :----------------------------------------------------------: |
|  find(子串，开始下标，结束下标)   | 检测子串是否包含在字符串里，如果存在就返回子串开始的下标，否则返回-1 |
|  index(子串，开始下标，结束下标)  | 检测子串是否包含在字符串中，如果存在就返回子串开始的下标，否则报错 |
|              rfind()              |         和find()功能相同，但查找方向从字符串右侧开始         |
|             rindex()              |        和rindex()功能相同，但查找方向从字符串右侧开始        |
|  count(子串，开始下标，结束下标)  |                返回子串在字符串中出现了的次数                |
| replace(旧子串，新子串，替换次数) |                  新子串替换字符串内的旧子串                  |
|       split(分割字符，num)        |                    按照指定字符分割字符串                    |
|     join(多字符串组成的序列)      |               用一个字符或子串合并为新的字符串               |
|           capitalize()            |                   将字符串第一个字母转大写                   |
|              title()              |               将字符串中每个单词的首字母转大写               |
|              lower()              |                     将字符串中大写转小写                     |
|              upper()              |                     将字符串中小写转大写                     |
|             lstrip()              |                    删除字符串左侧空白字符                    |
|             rstrip()              |                    删除字符串右侧空白字符                    |
|              strip()              |                    删除字符串两侧空白字符                    |









# 0904-容器

#### 列表

````python
# append() 可以给列表添加单个值
print("="*10 + "append" + "="*10)
name_list = ['小红', '小明', '张三']
print(name_list)
name_list.append('班长')
print(name_list)

# extend() 可以给列表添加多个值，会拆分传进来的参数
print("="*10 + "extend" + "="*10)
name_list1 = ['小红', '小明', '张三']
name_list1.extend(['组长', '班长'])
print(name_list1)

# insert() 可以给列表指定位置添加单个值
print("="*10 + "insert" + "="*10)
name_list2 = ['小红', '小明', '张三']
name_list2.insert(1, '组长')
print(name_list2)

# del() 删除列表中指定位置的值 或者 删除整个列表
print("="*10 + "del" + "="*10)
name_list3 = ['小红', '小明', '张三']
del name_list3[1]
print(name_list3)
del name_list3
# print(name_list3)

# pop()返回并删除列表末尾的一个值
print("="*10 + "pop" + "="*10)
name_list4 = ['小红', '小明', '张三']
print(name_list4.pop())
print(name_list4)

# remove() 指定删除列表中的值
print("="*10 + "remove" + "="*10)
name_list5 = ['小红', '小明', '张三']
name_list5.remove('小明')
print(name_list5)

# clear() 情况列表中的数据
print("="*10 + "clear" + "="*10)
name_list6 = ['小红', '小明', '张三']
name_list6.clear()
print(name_list6)

# 直接修改值
print("="*10 + "修改" + "="*10)
name_list7 = ['小红', '小明', '张三']
name_list7[1] = '小白'
print(name_list7)

# 将列表中的值倒序过来（从后往前）
print("="*10 + "reverse" + "="*10)
name_list8 = ['小红', '小明', '张三']
name_list8.reverse()
print(name_list8)

# 将列表中的数据按字母顺序进行排序
print("="*10 + "sort" + "="*10)
name_list9 = ['小红',  '小黑', '小明', '张三',  '小吖']
name_list9.sort()
print(name_list9)

# 判断列表中是否有值
print("="*10 + "in" + "="*10)
name_list0 = ['小红',  '小黑', '小明', '张三',  '小吖']
print('小黑' in name_list0)

````



#### 字典

````python
# 创建字典
dict1 = {}
dict2 = dict()
dict3 = {'name': '张三', 'age': '18', 'phone': '13333333333'}
print(type(dict1))
print(type(dict2))
print(type(dict3))

# 如果有同名的数据就修改，没有就增加
dict3['name'] = '胜雪'
print(dict3)
dict3['eyeColor'] = 'blue'
print(dict3)

print("="*10 + "获取" + "="*10)
print(dict3.get('from'))  # 获取数据没有就返回空
# print(dict3['from'])  # 获取数据没有就会报错
print(dict3.keys())
print(dict3.values())
print(dict3.items())

print("="*10 + "删除" + "="*10)
del dict3['name']
print(dict3)

print("="*10 + "清空数组" + "="*10)
dict3.clear()
print(dict3)
````





# 0905-条件/循环语句

#### 选择结构

> if 表达式:
>
> ​	语句体
>
> elif 表达式:
>
> ​	语句体
>
> elif 表达式:
>
> ​	语句体
>
> else:
>
> ​	语句体

![image-20210904184919543](笔记.assets/image-20210904184919543.png)

````python
#  选择结构
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
````





#### 循环结构

>  while 条件语句:
>
> ​	代码块
>
> 
>
> for 条件语句:
>
> ​	代码块



​	

> 循环体中应有使循环趋向于结束的语句，否则会出现死循环



##### while 循环

````python
# while 循环
a = 1
b = 0
while a <= 100:
    b += a
    a += 1
print(f'a的值是{a}，1~100的和是：{b}。')
````

##### for 循环

```python
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
```

##### 嵌套循环

```python
# 嵌套循环
tmp = [
    ['1', '2', '3'],
    ['11', '22', '33'],
    ['111', '222', '333'],
    ['1111', '2222', '3333'],
]
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
for a, count in enumerate(tmp):
    print(f'周{a+1}观看指南：')
    for name in count:
        print(name)
```



#### 跳出循环

> break 代表强行结束整个循环结构

```python
# 遇到break 就跳出循环 再也不执行了
i = 1
while True:
    if i == 5:
        print('到了')
        break
    print('没到')
    i += 1
```

> continue 代表结束本次循环，继续下一次循环

```python
# 遇到continue 跳出现在的这次循环，去继续执行下一次
for i in range(10):
    num = randint(3, 10)
    print(f'第{i+1}集，评分是：{num}')
    print('点赞')
    if num < 6:
        continue
    print('投币')
```

#### else和循环搭配

```python
from random import randint
print('坐公交车：')
# break 属于非正常结束，不执行下方代码else后面的
# i = 1
# while True:
#     if i == 5:
#         print('到了，下车！')
#         break
#     print('没到')
#     i += 1
# else:
#     print('终于到了')


# continue 属于正常结束循环，下方代码else中的语句也会的执行
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        print('到了，下车！')
        continue
    print('没到')
else:
    print('终于到了')
# continue 属于正常结束循环，下方代码else中的语句也会的执行
for i in range(10):
    num = randint(3, 10)
    print(f'第{i+1}集，评分是：{num}')
    print('点赞')
    if num < 6:
        continue
    print('投币')
else:
    print('终于看完了10集')
```

> 区别：
>
> continue 属于正常结束循环，下方代码else中的语句也会的执行
>
> break 属于非正常结束，不执行下方代码else后面的、





# 0906-函数的使用

#### 定义格式

- **使用关键字`def`定义**
- 函数名符合标识符规范
- 参数数量可以是任意个
- 语句体就是功能代码
- 返回值不是必须的。函数可以没有返回值

```python
def fun1():  # 无参数
    print('hello world')
fun1()


def fun2(info1):  # 1个参数
    print(f'hello {info1}！')
fun2('tom')


def fun3(info2, info3):  # 多个参数
    print(f'hello {info2, info3}！')
fun3('tom', 'jerry')


def fun4(*aaa):  # 任意N个参数
    for i in aaa:
        print(i)
fun4(1, 5, 3, 6, 9, 7)


def fun5(**ccc):       # name = allen    age = 18
    print(type(ccc))
    print(ccc.get('name'))
    print(ccc.get('age'))
fun5(name='allen', age=18)


def fun6(a: int, b: int):     # 传入int类型 的参数
    print(a+b)
fun6(9, 11)


def fun7(a1: str, a2: str = '投币'):    # 设置默认参数，也可以进行覆盖
    print(f'记得{a1}和{a2}')
fun7('点赞')
fun7('点赞', '转发')


def fun10(a, b):     # 有返回值
    return a + b
print(fun10(2, 9))
```





# 0907-面向对象



