#题目：将一个数组逆序输出。

#程序分析：用第一个与最后一个交换。

a = [1,2,3,4,5,6,7]
l=len(a)
middle = l//2
for i in range(0,middle):
    a[i],a[l-1-i] = a[l-1-i], a[i]
print(a)
