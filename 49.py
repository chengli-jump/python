#题目：使用lambda来创建匿名函数。

maxnum = lambda x,y :(x>y)*x+(x<y)*y
minnum = lambda x,y :(x<y)*x+(x>y)*y

if __name__ ==  '__main__':
    a = 10
    b = 20
    print(maxnum(a,b))
    print(minnum(a,b))