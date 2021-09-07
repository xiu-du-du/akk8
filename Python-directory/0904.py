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


#  字典
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

# 作业一：
info = [8, 8.5, 9, 9.5, 8.2, 10, 6, 8.8, 9.2, 8.2]
info.sort()
del info[0]
del info[-1]
print(info)

# 作业二：
fan1 = {'name': '东皇战影', '评分': '9.1 分', '发布时间': '2016年5月25日'}
fan2 = {'name': '黑白龙狼传', '评分': '9.5 分', '发布时间': '2009年8月8日'}
fan3 = {'name': '魔戮血战', '评分': '9.7 分', '发布时间': '2014年1月15日'}
print(fan1)
print(fan1.keys())
print(fan1.values())
print(fan1.items())

print(fan2)
print(fan3.keys())
print(fan3.values())
print(fan3.items())

print(fan3)
print(fan3.keys())
print(fan3.values())
print(fan3.items())






