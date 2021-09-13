# 当前时间:2021/9/13 18:57
"""
列表的创建
"""
lst1=['hello','world',899]   # 使用[]直接创建
lst2=list(['hello','world',899,'hello'])   # 使用内置函数list()

"""
列表的特点
1. 列表元素按顺序有序排序
2. 索引映射唯一个数据
3. 列表可以存储重复数据
4. 任意数据类型混存
5. 根据需要动态分配和回收内存
"""
print(id(lst2[0]))
print(id(lst2[-4]))
print(lst2.index('hello'))
print(lst2.index('hello',1))

'''
列表的查询
1. 获取列表中指定元素的索引 index()
    a. 如列表中存在N个相同元素，只返回第一个元素的索引
    b. 如元素再列表中不存在，则会报错
    c. 可以在制定的start和end之间查找
2. 获取列表中的单个元素
    a. 正向索引从0到N-1  
    b. 逆向索引从-N到-1
    c. 指定索引不存在，则会报错
3. 获取列表中的多个元素
'''
# 切片操作
# 切出来的lst4是新的列表对象
lst3=[10,20,30,40,50,60,70,80]
lst4=lst3[1:6:1]
print(id(lst3))
print(id(lst4))
print(lst3[::-1])
print(lst3[::2])
# in 判断是否存在
# not in 判断是否不存在
print('o' in 'python')
print('s' in 'python')
print(10 in lst3)
print(100 in lst3)
print(10 not in lst3)
print(100 not in lst3)
# 遍历列表
for i in lst3:
    print(i)
# 列表元素的增删改
# append() 在列表末尾添加一个元素
lst3.append(22)
lst5=lst3
print(lst3)
print(id(lst3))
print(lst5)
print(id(lst5))
# 将整个列表添加
lst3.append(lst2)
print(lst3)
# extend() 将列表中的元素添加
lst3.extend(lst2)
print(lst3)
# insert() 在指定位置添加元素
lst3.insert(1,90)
print(lst3)
# 切片 从指定位置开始切，然后添加元素
lst3[1:]=lst2
print(lst3)

# 列表删除
# remove() 从列表中移除一个元素，如果有重复，只移除第一个，不存在则报错
lst3.remove(10)
print(lst3)
# pop() 根据索引移除元素,如果不写索引则会删除末尾的一个元素,如果索引不存在，则会报错
lst3.pop(1)
print(lst3)
# 切片
# 产生新对象
lst6=lst3[1:2]
print(id(lst3))
print(id(lst6))
lst3[1:2]=[]
print(lst3)
# clear() 清空列表
lst3.clear()
print(lst3)
lst3=[10,20,30,40,50,60,70,80]
# del 删除列表对象
# 删除后需要重新定义
del lst3
# print(lst3)

# 列表的修改
# 指定索引修改元素
lst3=[10,20,30,40]
lst3[2]=500
print(lst3)
# 切片
# 指定N个元素修改
lst3[1:3]=[300,500,800,900]
print(lst3)

# 列表元素排序
# 升序
lst3.sort()
print(lst3)  # 从小到大排序
lst3.sort(reverse=False)
print(lst3)  # 从小到大排序
# 降序
lst3.sort(reverse=True)
print(lst3)  # 从大到小
print("===="*20)
print(lst3)
lst7=sorted(lst3)  # 升序
print(lst7)
lst8=sorted(lst3,reverse=True)  # 降序
print(lst8)

# 列表生成式
lst=[i*2 for i in range(1,6)]
print(lst)

