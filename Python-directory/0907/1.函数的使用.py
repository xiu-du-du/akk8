print('allen')
def fun1():  # 无参数
    print('hello world')
fun1()

def fun2(info1):  # 1个参数
    print(f'hello {info1}！')
fun2('tom')

def fun3(info2, info3):  # 多个参数
    print(f'hello {info2, info3}！')
fun3('tom', 'jerry')

def fun4(*aaa):  # 任意N个参数
    for i in aaa:
        print(i)
fun4(1, 5, 3, 6, 9, 7)

def fun5(**ccc):       # name = allen    age = 18
    print(type(ccc))
    print(ccc.get('name'))
    print(ccc.get('age'))
fun5(name='allen', age=18)

def fun6(a: int, b: int):     # 传入int类型 的参数
    print(a+b)
fun6(9, 11)

def fun7(a1: str, a2: str = '投币'):    # 设置默认参数，也可以进行覆盖
    print(f'记得{a1}和{a2}')
fun7('点赞')
fun7('点赞', '转发')

def fun10(a, b):     # 有返回值
    return a + b
print(fun10(2, 9))


