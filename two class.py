class stud:
    def __init__(self,a,b,c):
        self.name=a
        self.sno=b
        self.age=c
    def disp(self):
        print("student sno:", self.name)
        print("student name:",self.sno)
        print("student age:",self.age)
class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super().__init__(a,b,c)
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def disp(self):
        super().disp()
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)

ob=marks(123,'gokul',18,45,66,77)
ob.disp()
        
        
        



           
