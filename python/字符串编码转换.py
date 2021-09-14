# 当前时间:2021/9/14 20:19
# 编码
s='天涯共此时'
print(s.encode(encoding='GBK'))   # GBK编码中一个中文占2个字符
print(s.encode(encoding='UTF-8'))   # UTF-8编码中一个中文占3个字符

# 解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))



