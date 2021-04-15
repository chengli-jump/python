#题目：输入三个整数x,y,z，请把这三个数由小到大输出
alist = []
for i in range(8):
    x = int(input())
    alist.append(x)

for i in range(0, len(alist)):
    for j in range(len(alist)-1,i,-1):
        if alist[j] < alist[i]:
            alist[j],alist[i] = alist[i], alist[j]
print(alist)
