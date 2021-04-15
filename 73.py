#题目：反向输出一个链表。


if __name__ ==  '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a nunber:\n'))
        ptr.append(num)

    for i in range(len(ptr)-1,-1,-1):
        print(ptr[i])