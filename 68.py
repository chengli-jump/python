#题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
m = 3
a = [1,2,3,4,5,6,7]

def rot(a,n):
    l = len(a)
    n = l-n
    return a[n:l] + a[0:n]
b = rot(a,m)
print(b)