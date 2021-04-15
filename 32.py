#题目：按相反的顺序输出列表的值

#数据结构栈反转序列
'''
alist = ['a','b','c']

print(alist[::-1])
'''
#pop()返回列表当前尾部数据
num = list(range(10))
revernum = []
for i in range(10):
    revernum.append(num.pop())

print(revernum)