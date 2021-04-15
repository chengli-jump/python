#题目：输入某年某月某日，判断这一天是这一年的第几天？

#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
#利用数轴储存天数

year = int(input('year：'))
mouth = int(input('mouth: '))
day = int(input('day: '))

mouths = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < mouth <= 12:
    sum = mouths[mouth-1]
else:
    print('data error')

sum += day

#立个判断瑞年的flag
flag = 0
if (year%400==0) or ((year % 4== 0) and (year % 100 !=0)):
    flag = 1
if (flag==1) and (mouth>2):
    sum+=1

print(sum)