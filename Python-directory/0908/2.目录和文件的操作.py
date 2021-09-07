# 当前时间： 2021-09-06 20:20
import os
os.makedirs('tmp') #创建目录
os.rmdir('tmp') #删除目录

# f=open('aaa.py','a') #创建一个aaa.py文件，然后设置模式(w=write模式;a=add模式)
# f.write("a='hello word'\n")
# f.write('b=1\n')
# f.write('c=2\n')
# f.write('d=3\n')
# f.close()
#
###这种写法会自动关闭，不需要写关闭
# with open('aaa.py','a') as f:
#     f.write("a='hello word'\n")
#     f.write('b=1\n')
#     f.write('c=2\n')
#     f.write('d=3\n')
#
# with open('aaa.py','r') as f:
#     # print(f.read(10))  #读取指定字节内容
#     # print(f.readline() ) #读取一行
#     # print(f.readlines())  #读取所有行

# with open('logo.png','rb') as f:  #r=read模式 b=byte字节
#     print(f.read())

# f1= open('logo.png','rb')
# f2= open('logo2.png','wb')
# f2.write(f1.read())
# f2.close()
# f1.close()


with open('logo2.png','wb') as f2:
    f1=open('logo.png','rb')
    f2.write(f1.read())
