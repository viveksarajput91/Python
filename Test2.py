import math as m
x=[1,2,3,4,7,9,10,13,17,19,20,24]
for y in range(0,x.__len__()):
    if(x[y]==1):
        continue
    if(x[y]==2):
        print(x[y])
        continue
    if(x[y] > 2 and x[y]%2==0):
        continue
    sqr= m.floor(m.sqrt(x[y]))
    for z in range(2,sqr+1,1):
        if(x[y]%z==0):
            break
    else:
        print(x[y])
