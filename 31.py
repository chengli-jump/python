#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

#采用字典存储数据
#list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
'''
weeklist = {'M':'Monday', 'T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday','F':'Friday','S':{'a':'Saturday','u':'Sunday'}}

a = input('请输入首字母:')
a = a.upper()

if a in ['T','S']:
    b = input('请输入第二字母:')
    print(weeklist[a][b])
    

else:
    print(weeklist[a])
'''
