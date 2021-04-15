#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

#典型的菲波数列

def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(12))

def fibs(n):
    if n == 1:
        return [1]
    elif n == 2:
        return[1,1]
    fibs = [1,1]
    for i in range (2,n+1):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs
print(fibs(12))