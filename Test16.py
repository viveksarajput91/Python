class Numbers:
    def __init__(self):
        self.num=[1,2,3,5,8,3,9]
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.num):
            val=self.num[self.i]
            self.i+=1
            return val
        else:
            raise StopIteration()


numbers2=Numbers()
for k in numbers2:
    print(k)