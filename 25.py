#题目：求1+2!+3!+...+20!的和。
#程序分析：此程序只是把累加变成了累乘。
def a(n):
    if n==1:
        return 1
    return n*a(n-1)


b = [a(i) for i in range(1,21)]
print(sum(b))

'''
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)
'''