class Person:
    def __init__(self,fname,Iname):
        self.fname=fname
        self.Iname=Iname
    def Personname(self):
        print(f"Fist name :{self.fname} last name:{self.Iname}")
    

x=Person("jone","fff")
x.Personname()
        
    