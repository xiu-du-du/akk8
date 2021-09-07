# 当前时间： 2021-09-06 20:49
# 作业一：
i=0
with open('text.txt','w') as f1:
    while i<51:
        f1.write(f'192.168.1.{i}\n')
        i += 1







# 作业二：
with open('text.txt','r') as f2:
    list1=f2.readlines()
    a=0
    for i in range(len(list1)):
        if list1[i] == '192.168.1.6\n':
            a +=1
        i += 1
    print(f'出现了{a}次')