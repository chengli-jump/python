def quicksort(a):
    for i in range(len(a)-1,1,-1):
        maxpos = 0
        for j in range(1,i+1):
            if a[j] > a[maxpos]:
                maxpos = j
        a[maxpos],a[i] = a[i], a[maxpos]

    return a

a = [1,3,7,2,6,5,4]
print(quicksort(a))