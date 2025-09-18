class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.name=a
        self.sno=b
        self.age=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        tot=m1+m2+m3
        avg=tot/3
        if m1>=40 and m2>=40 and m3>=40:
            self.result="pass"
        else:
            self.result="fail"
    def disp(self):
        print("student sno:", a)
        print("student name:",b)
        print("student age:",c)
        print("mark1:",m1)
        print("mark2:",m2)
        print("mark3:",m3)
a=int(input("enter the value:"))
b=input("enter the value:")
c=int(input("enter the value:"))
m1=int(input("enter the value:"))
m2=int(input("enter the value:"))
m3=int(input("enter the value:"))
ob=stud(a,b,c,m1,m2,m3)
ob.calculate()
ob.disp()
