# 当前时间:2021/9/13 21:01

# 可变序列
# 列表，字典
lst=[10,20,30]
print(id(lst))
lst.append(40)
print(id(lst))

# 不可变序列
# 字符串，元祖
s='hello'
print(id(s))
s=s+'world'
print(id(s))

