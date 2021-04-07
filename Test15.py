class employee:
    def __init__(self,Salary):
        self.Salary=Salary
    def __add__(self, other):
        return employee(self.Salary + other.Salary)
    def display(self,val=None):
        if(val !=None):
            return val
        else:
            return "blank name provided"


e1=employee(65000)
e2=employee(75000)
e3=employee(80000)
print(e1.Salary)
print(e2.Salary)
print(e3.Salary)
print(f"Employee 1 salary {e1.Salary} and Employee 2 salary is {e2.Salary} and sum of both is {(employee(e1.Salary)+e2+e3).Salary}")
print(e1.display())

