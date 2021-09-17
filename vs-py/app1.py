# 当前时间:2021/9/17 21:03
# 三元运算符
age = 22
message = "Eligible" if (18 < age or age < 25) and age == 22 else "Not eligible"
print(message)

for x in range(5):
    for y in range(3):
        print(f'({x},{y})')

n = 100
n //= 2  # //整数 /浮点
print(n)

while True:
    command = input('>')
    print("ECHO", command)
    if command.lower() == 'quit':
        break

for i in range(2, 10, 2):
    print(i)
print('i', i)

count=0
for i in range(1, 10):
    if i%2==0:
        count+=1
print(count, i)

def greet():
    print('1')
greet()

