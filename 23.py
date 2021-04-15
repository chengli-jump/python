'''  
   *
  ***
 *****
*******
 *****
  ***
   *
   '''
#1,3,5,7 -> 2(n+1)-1
#3,2,1,0
#5,3,1 ->0,1,2->2(3-i)-1
for i in range(4):
    print('\n')
    for k in range(3-i):
        print(' ',end="")
    for j in range(2*(i+1)-1):
        print('*',end="")

for i in range(3):
    print('\n')
    for k in range(i+1):
        print(' ',end="")
    for j in range(2*(3-i)-1):
        print('*',end="")

        

