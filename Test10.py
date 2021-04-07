from functools import *

listNumbers=[1,2,3,4,5,6,7,8,9]
resultOddNumbers=list(filter(lambda n:n%2 !=0,listNumbers))
print(resultOddNumbers)

resultMaps=list(map(lambda n:n*2,list(filter(lambda n:n%2 !=0,listNumbers))))
print(resultMaps)

resultReduce= reduce(lambda a,b:a+b,list(map(lambda n:n*2,list(filter(lambda n:n%2 !=0,listNumbers)))))

print(resultReduce)