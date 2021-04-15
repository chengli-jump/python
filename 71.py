#题目：编写input()和output()函数输入，输出5个学生的数据记录。

#stu
# num : string
# name : string
# score[4]: list

class Student:
    name=''
    age=0
    score = [None] * 4

    def input(self):
        self.name = input('Input name:')
        self.age = int(input('input age:'))
        for i in range(len(self.score)):
            self.score[i] = int(input('input score:'))
    
    def output(self):
        print('output name %s'% self.name)
        print('output age %d' % self.age)
        for i in range(len(self.score)):
            print('output %d score is %d'%(i+1,self.score[i]))
if __name__ == '__main__':
    N = 3
    studentarray = [Student()] * N
    for i in range(len(studentarray)):
        studentarray[i].input()
    for i in range(len(studentarray)):
        studentarray[i].output()

        
