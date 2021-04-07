class outerClass:
    def __init__(self,className):
        self.OuterClassName=className
        self.InnerClassName=self.innerClass("Inner Class").Name

    class innerClass:
        def __init__(self,className):
            self.Name=className

o=outerClass("Outer Class")
print(o.OuterClassName)
print(o.InnerClassName)