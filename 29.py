#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

x = int(input('请输入'))
a = x%10
b = x%100//10
c = x%1000//100
d = x%10000//1000
e = x//10000

if e!= 0:
    print('5位数：',e,d,c,b,a)

elif d!= 0:
    print('4位数：',d,c,b,a)

elif c!= 0:
    print('3位数：',c,b,a)

elif b!=0:
    print('2位数：',b,a)

elif a!= 0:
    print('1位数：',a)