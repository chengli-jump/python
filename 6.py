#题目：斐波那契数列。
#分析
'''
F0 = 1     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
#1、1、2、3、5、8、13、21、34、……
#递归
def fib(n):
    if n==1 or n==2: #递归出口
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))

def fibs(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

print(fibs(10))