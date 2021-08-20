class Emp:
    empno=0
    salary=0
    grade=''
    #parameterized 
    def _init_(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('Const. called')
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
    def _del_(self):
        print('Bye...')
obj1=Employee(101,43000,'B')
#_init_ calls
obj1.show()
obj2=Employee(102,41000,'A')
obj2.show()
        
        