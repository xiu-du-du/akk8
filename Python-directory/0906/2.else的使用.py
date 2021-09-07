from random import randint
print('坐公交车：')
# break 属于非正常结束，不执行下方代码else后面的
# i = 1
# while True:
#     if i == 5:
#         print('到了，下车！')
#         break
#     print('没到')
#     i += 1
# else:
#     print('终于到了')

# continue 属于正常结束循环，下方代码else中的语句也会的执行
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        print('到了，下车！')
        continue
    print('没到')
else:
    print('终于到了')

# continue 属于正常结束循环，下方代码else中的语句也会的执行

for i in range(10):
    num = randint(3, 10)
    print(f'第{i+1}集，评分是：{num}')
    print('点赞')
    if num < 6:
        continue
    print('投币')
else:
    print('终于看完了10集')