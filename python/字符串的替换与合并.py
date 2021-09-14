# 当前时间:2021/9/14 19:42
# replace(字符串，子串，次数)  替换字符串
s='hello,python'
print(s.replace('python','world'))
s='hello,python,python,python'
print(s.replace('python','world',2))

# join() 将列表或元祖中的字符串合并成一个新字符串
# 列表
lst=['hello','python','world']
print(' '.join(lst))
# 元祖
t=('hello','python','world')
print(' '.join(t))
# 直接连接字符串
print('*'.join('hello'))

