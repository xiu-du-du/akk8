# 当前时间:2021/9/14 19:51
# 原始值比较
print(ord('a'),ord('b'))   # 获取原始值
print(ord('张'),ord('小'))
print(chr(97),chr(98))    # 原始值转换
print(chr(24352),chr(23567))
print('apple'>'app')   # True
print('apple'>'banana')   # False

'''
== 和 is 的区别:
== : 比较的是value
is : 比较的是id
'''
a=b='python'
c='python'
print(a==b)
print(b==c)
print(a is b)
print(b is c)
print(id(a),id(b),id(c))
