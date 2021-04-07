from array import *
arr=array("i",[5,3,4,1,2])
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        temp=0
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for k in range(len(arr)):
    print("Array in ascending order " + str(arr[k]))
