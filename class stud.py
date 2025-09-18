class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def disp(self):
        print("student no:",self.sno)
        print("student name:",self.name)
        print("student age:",self.age)
x=int(input("enter the value:"))
y=input("enter the value:")
z=int(input("enter the value:"))
ob=stud(x,y,z)
ob.disp()

    
    
