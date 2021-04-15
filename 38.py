#题目：求一个3*3矩阵主对角线元素之和。

import numpy as np  


a = np.array([
    [1,3,4],
    [1,3,4],
    [1,3,4],
]) 

sum=0
for i in range(0,3):
    sum = sum+a[i][i]
print(sum)

