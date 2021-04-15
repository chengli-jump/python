#题目：画图，学用matplotlib画圆形。

import math as m
import matplotlib.pyplot as plt

x=[]
y=[]
for a in range(1,11):
    for b in range(0,360):
        x.append(a*(m.cos(m.pi*(b/180))))
        y.append(a*(m.sin(m.pi*(b/180))))
plt.scatter(x,y,s=30)
plt.axis([-11,11,-11,11])
#避免因比例而压缩为椭圆
plt.axis('equal') 
plt.show()