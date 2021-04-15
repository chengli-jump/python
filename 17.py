#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

#程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
astring = input('输入一串字符')
zimu=0
kongge=0
digit=0
qita=0
position = len(astring)-1
while position>0:
    if astring[position].isalpha():
        zimu += 1
        position -= 1
    elif astring[position].isspace():
        kongge += 1
        position -= 1
    elif astring[position].isdigit():
        digit += 1
        position -= 1
    else:
        qita += 1
        position -= 1
print('char=%d,space=%d,digit=%d,others=%d'%(zimu,kongge,digit,qita))
        
    
    