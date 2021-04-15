#判断101-200之间有多少个素数，并输出所有素数。
#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
from math import sqrt
count = 0
alist = []
flag = 1
for num in range(101,201):
    for i in range (2,int(sqrt(num))+1):
        if (num%i==0):
            flag = 0
            break
    if flag == 1:
        count += 1
        alist.append(num)
    flag = 1

print(alist)
print(count)
