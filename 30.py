#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#栈这种数据结构可以逆序数据
#python list内置逆序遍历
a = input('请输入')
flag = True

for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        flag=False
        break
if flag:
    print('回文')
else:
    print('不是回文')