#题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组

def findmaxmin(a):
    maxpos = 0
    minpos = 0
    for i in range (len(a)-1,1,-1):
        if a[i] > a[maxpos]:
            maxpos = i
        if a[i] < a[minpos]:
            minpos = i
    print(maxpos,minpos)
    a[0],a[minpos] = a[minpos], a[0]
    a[len(a)-1], a[maxpos] = a[maxpos], a[len(a)-1]
    return a

a = [2,4,3,1,8,7,6,5]
print(findmaxmin(a))