from array import *
arr=array("i",[])
s=int(input("please enter the size of the array"))
for i in range(s):
    a=int(input("Please enter " + str(i) + " array value"))
    arr.append(a)
print(arr)

k=0
indexvalue=int(input("Please enter array value"))
for j in arr:
    if(j==indexvalue):
        print(k)
        break
    k+=1
