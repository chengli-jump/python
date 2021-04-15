#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

#程序分析：请抓住分子与分母的变化规律。
def a(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return a(n-1)+a(n-2)

def b(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return b(n-1)+b(n-2)

s = [a(i)/b(i) for i in range(1,21)]
print(sum(s))
