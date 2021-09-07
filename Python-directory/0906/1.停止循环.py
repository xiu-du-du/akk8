from random import randint

# 遇到break 就跳出循环 再也不执行了
i = 1
while True:
    if i == 5:
        print('到了')
        break
    print('没到')
    i += 1

# 遇到continue 跳出现在的这次循环，去继续执行下一次
for i in range(10):
    num = randint(3, 10)
    print(f'第{i+1}集，评分是：{num}')
    print('点赞')
    if num < 6:
        continue
    print('投币')

