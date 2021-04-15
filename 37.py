#题目：对10个数进行排序。
a = [1,4,5,6,2,3,8,7,9,19]

def selectsort(alist):
    for i in range(len(alist)-1,0,-1):
        maxpos = 0
        for j in range(1,i+1):
            if alist[j] > alist[maxpos]:
                maxpos = j
        alist[maxpos],alist[i] = alist[i],alist[maxpos]
    return alist

print(selectsort(a))


'''
#sort方法
a.sort()
print(a)
'''


            
