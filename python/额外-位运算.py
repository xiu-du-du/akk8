# 当前时间： 2021-09-08 19:46
#位运算
#按位与 &   按位或 |   按位左移<<    按位右移>>
a=23
b=15
print(a & b)   #7  换算成二进制，同为1都为1，否则为0
print(a | b)   #31 只要有一个为1，就位1，否则为0
print(a ^ b)   #24 不同为1，相同为0

x=5
print(x << 2)   #20 左移公式：a<<n ==> a*2的n次方
print(x >> 2)   #20 右移公式: a>>n ==> a/2的n次方，右移会将最右边的移出去，导致丢失数据

# 运用举例：
color=0xf0384e
red=color >> 16
print(hex(red))
green=color >> 8 & 0xFF
print(hex(green))
blue=color & 0xFF
print(hex(blue))


