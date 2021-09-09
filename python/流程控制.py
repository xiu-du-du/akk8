# 当前时间： 2021-09-08 20:57
# 嵌套练习：乘法表
# row=1
# while row <10:
#     cell=1
#     print()
#     while cell <= row:
#         if row*cell<10:
#             print(f'{cell} x {row} = {row * cell}', end='    ')
#         else:
#             print(f'{cell} x {row} = {row*cell}',end='   ')
#         cell+=1
#     row+=1


#判断练习
# age=int(input('输入年龄：\n'))
# if age <18:
#     print('未成年人')
# elif 60>age>=18:
#     print('成年人')
# elif 150>=age>=60:
#     print('老年人')
# else:
#     print('这不是人！')

#循环练习
# a=0
# for i in range(0,101):
#     a+=i
# print(a)

num=0
for i in range(0,101):
    if i%10==2 :
        if i%3==0:
            num+=1
print(num)