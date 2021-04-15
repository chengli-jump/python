#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。  
k = []
for j in range(2,1001):
    for i in range(1,j):
        if j%i == 0:
            k.append(i)
    if j==sum(k):
        print(j)
    k=[]
    

    