#题目：求100之内的素数。

for i in range(1,101):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
    