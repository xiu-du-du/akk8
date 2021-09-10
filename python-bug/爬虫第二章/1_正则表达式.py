# 当前时间:2021/9/11 0:03
import re
# # findall(正则表达式，要匹配的文本):匹配字符串中所有的符合正则的内容[返回的是列表]
# lst=re.findall(r'\d+','我的电话是：10086。你的电话是：10010。')
# print(lst)

# # finditer(正则表达式，要匹配的内容):匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容需要.group()
# it=re.finditer(r'\d+','我的电话是：10086。你的电话是：10010。')
# for i in it:
#     print(i.group())

# # search():找到一个结果就返回，返回的结果是match对象。拿数据需要.group()
# s=re.search(r'\d+','我的电话是：10086。你的电话是：10010。')
# print(s.group())

# # match():从字符串的开头开始匹配。拿数据需要.group()
# s=re.match(r'\d+','我的电话是：10086。你的电话是：10010。')
# print(s.group())

# # 预加载正则表达式
# obj=re.compile(r'\d+')   # 提高效率：先提前加载好正则，等用的时候再用
# ret=obj.finditer('我的电话是：10086。你的电话是：10010。')
# for i in ret:
#     print(i.group())

ss="""
<div class='jay'><span id='1'>郭金</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""

# re.S: 让.能匹配换行符
# (?P<分组名称>正则) 可以单独从正则匹配的内容中进一步提取内容
obj=re.compile(r"<div class='(.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)   # 提高效率：先提前加载好正则，等用的时候再用
aa=obj.finditer(ss)
for i in aa:
    print(i.group('id'),end='    ')
    print(i.group('name'))
