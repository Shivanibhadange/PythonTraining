'''
class Employee:
    empno=0
    name=''
    def get(self,a,b):
        self.empno=a
        self.name=b
    def show(self):
        print(self.empno)
        print(self.name)
        
obj=Employee()
obj.get(101,'Raj')
obj.show()
obj1=Employee()
obj1.get(102,'Amit')
obj1.show()

class Employee:
    empno=0
    salary=0
    grade=''
    def get(self,a,b):
        self.empno=a
        self.salary=b
    def check(self):
        if self.salary>=30000:
            self.grade='A'
        else:
            self.grade='B'
    def show(self):
        self.check()
        print(self.empno)
        print(self.grade)
obj=Employee()
obj.get(103,31000)
obj.show()

    
    '''
class Employee:
    empno=101
    salary=21000
    grade='A'
obj=Employee()
print(hasattr(obj,'empno')) #true
print(getattr(obj, 'salary'))
print(obj,'salary',45000) 
print(getattr(obj, 'salary'))  
#delattr(obj, 'empno')
#print(hasattr(obj, 'empno')) #False    
    