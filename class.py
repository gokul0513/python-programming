class bike:
    def __init__(self,x,y,z):
        self.numberplate=x
        self.color=y
        self.brand=z
    def disp(self):
        print(self.numberplate)
        print(self.color)
        print(self.brand)
ob=bike("tn042024","black","dio")
ob.disp()
    
