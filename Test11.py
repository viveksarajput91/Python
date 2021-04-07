def divison(a,b):
    print(a/b)


def innerfunction(a,b):
    if a<b:
        a,b=b,a
    return divison(a,b)

if(__name__=="__main__"):
    divisonResult= innerfunction(10,50)
    print(__name__)