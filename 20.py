#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#a1=100*0.5 ...an=100*(0.5)^n
#s1=100,s2=a1*2,s3=a2*2
import math
n = int(input('请输入下落次数'))
a = []
a = [100*pow(0.5,i) for i in range(1,n+1)]
print(a)
s = []
s.append(100)
for i in range(1,n+1):
    s.append(a[i-1]*2)
print(sum(s))