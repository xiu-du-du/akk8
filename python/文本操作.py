# 当前时间:2021/9/13 6:59

# index() 与find()的作用相同，但如果没找到会直接报错
# find() 从左向右查找字符串，遇到一个符合要求的则返回位置。如果没有找到则返回-1。
# rfind() 从右向左查找字符串，遇到一个符合要求的则返回位置。如果没有找到则返回-1。
path='https://ali-imgs.acfun.cn/kos/nlav10360/static/common/' \
    'widget/header/img/acfunlogo.11a9841251f31e1a3316.svg'
print(path[path.rfind('/')+1:][path[path.rfind('/')+1:].find('.')+1:])

# count() 查找字符串内字符的个数
print(path.count('.'))

# 判断类：startswith,endswith,isalpha,isdigit,isalnum,isspace
# startswith() 是否以'xxx'开头
print(path.startswith('ht'))
# endswith() 是否以'xxx'结尾
print(path.endswith('svg'))
# isdigit() 是否是

