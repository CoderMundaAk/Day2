#💼 Project 2 (Bonus): Employee / Manager Inheritance
class Empolyee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_info(self):
        print(f" Empolyee name {self.name} Empolyee Salary:{self.salary}")

class Manager(Empolyee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        super().display_info()
    def team_size(self):
        print("total team size : 25")
    def hire_employee(self):
        print(" The total hired empolyee is 5 ")
e=Empolyee("ak","444444")
m=Manager("bilal","55555555555555555555555555")
e.display_info()
# m.display_info()
m.hire_employee()