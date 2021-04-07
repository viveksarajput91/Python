class parent1:
    def __init__(self):
        self.Name="Parent 1 Class"
        print(self.Name)

class parent2:
    def __init__(self):
        self.Name="Parent 2 Class"

class Child(parent1,parent2):
    def __init__(self):
        super().__init__()
        self.Name="Child Class"

c= Child()
print(c.Name)