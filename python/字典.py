# 当前时间:2021/9/13 20:19
# 字典
# 字典根据key查找value所在的位置
# 字典的创建
scores={'张三':100,"张四":89}
print(scores)
print(type(scores))

a=dict(name='jack',age=20)
print(a)

# 获取字典中的数据
print(scores.get('张四'))   # 如果不存在返回None
print(scores.get('小明',404))   # 如果不存在，可以设置默认值
print(scores['张四'])   # 如果不存在则会报错

# key的判断
print('张三' in scores)
print('张三' not in scores)

# key的删除
del scores['张三']
print(scores)
scores.clear()  # 清空字典
print(scores)

# 字典的增加
scores['小红']=50
print(scores)

# 字典的修改
scores['小红']=100
print(scores)


# 获取所有的key
scores={'张三':100,"张四":89,"小红":100}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))   # 将所有keys组成的视图转成列表

# 获取所有的values
values=scores.values()
print(values)
print(type(values))
print(list(values))   # 将所有values组成的视图转成列表

# 获取所有key-value对
items=scores.items()
print(items)
print(type(items))
# 将所有key-value对组成的视图转成列表
# 转换后的列表是由元祖组成的
print(list(items))


# 字典的常用操作
# 字典元素遍历
# 遍历字典里的key和value
for item in scores:
    print(item,scores[item],scores.get(item))

# 字典的特点
# 字典中key不允许重复，value可以重复
d={'name':'小明','name':'张三'}
print(d)
d={'name1':'张三','name2':'张三'}
print(d)
# 字典中元素是无序的
# 字典中key必须是不可变对象
# 字典可以根据需要动态伸缩
# 字典会耗费较多的内存空间

# 字典生成式
items=['Fruits','Books','Others']
prices=[96,78,85]
# zip() 可以打包成字典
# upper() 可以将小写转换成大写
d={item.upper():price for item,price in zip(items,prices)}
print(d)



