#题目：求输入数字的平方，如果平方运算后小于 50 则退出。

num = int(input('请输入一个数:'))
if num**2 >= 50:
    print(num**2)
else:
    print()