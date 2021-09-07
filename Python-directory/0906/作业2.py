i = 100
while i < 201:
    i += 1
    if i % 6 == 0:
        for a in range(10):
            print(i, end=" ")
        print("\n")
        continue
else:
    print('已经找到所有100~200之间能被6整除的数！')
