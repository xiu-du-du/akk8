# 作业一
def fun1(firstAge: int,nowAge: int=2050):
    return nowAge - firstAge
first = input('请输入出生年份：')
nowAge = input('请输入今年年份：')
print(fun1(int(first, nowAge)))

# 作业二
def fun2(info: list):
    for i in range(len(info)):
        if info[i].get("score") >= 9.5:
            print(info[i])
count = [
    {'name': '名侦探柯南', 'score': 9.8},
    {'name': '鬼灭之刃', 'score': 9.1},
    {'name': '无能力者娜娜', 'score': 9.4}
]
fun2(count)




