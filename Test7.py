from array import *
arr=array("i",[5,4,3,2,1])
reverseArray=array("i",[])
arrLength=len(arr)
for x in range(arrLength,0,-1):
    reverseArray.append(arr[x-1])
print(arr)
print(reverseArray)

