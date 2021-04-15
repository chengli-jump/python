#题目：统计 1 到 100 之和

def sum(a):
    if a == 1:
        return 1
    else:
        return a+sum(a-1)
print(sum(100))