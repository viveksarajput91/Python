from array import *
arry = array("i",[1,2,3,4,5])
newarry=array(arry.typecode,[i-1 for i in arry])
for x in newarry:
    print(x)