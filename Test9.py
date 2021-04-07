from numpy import *
x=array([[1,2],
         [3,4],
         [5,6],
         [7,8]
         ])
y=array([
            [1,2,3,4],
            [5,6,7,8]
         ]
        )

result=array([
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
              ])

z=matrix(x)*matrix(y)
print("Built in Result")
print(z)

print()

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i,j]+=x[i][k]*y[k][j]
print(result)