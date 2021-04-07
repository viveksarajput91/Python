class yieldClass:
    def __init__(self):
        self.Names=["Vivek","Shravan","Jigar","Kailash"]
        self.i=0
    def GetEmployeeName(self):
        while self.i < len(self.Names):
            yield self.Names[self.i]
            self.i+=1

y=yieldClass()
for j in y.GetEmployeeName():
    print(j)