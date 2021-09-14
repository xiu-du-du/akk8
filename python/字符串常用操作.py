# 当前时间:2021/9/14 19:29
# 分割
s1='hello world python'
lst1=s1.split()   # 不写参数默认用空格分隔
print(lst1)
s='hello|world|python'
lst=s.split('|')
print(lst)
print(s.split(sep='|',maxsplit=1))   # 从左边开始分

print(s.rsplit())
print(s.rsplit('|'))
print(s.rsplit(sep='|',maxsplit=1))   # 从右边开始分

# 判断
# isidentifier() 判断指定字符串是否为合法标识符
s2='hello,python'
print('1.',s2.isidentifier())
print('2.','hello'.isidentifier())
print('3.','张三_'.isidentifier())
print('4.','张三_123'.isidentifier())

# isspace() 判断指定字符串是否由空白字符组成
print('5.','\t'.isspace())
# isalpha() 判断指定字符串是否全部由字母组成
print('6.','abc'.isalpha())
# isdecimal() 判断指定字符串是否全部由十进制数字组成
print('7.','0123456789'.isdecimal())
# isnumeric() 判断指定的字符串是否全部由数字组成
print('8.','0123456789'.isnumeric())
# isalnum() 判断指定字符串是否全部由字母和数字组成
print('9.','012345a6789'.isalnum())


