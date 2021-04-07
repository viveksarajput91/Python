listnumber=100
x=[True for j in range(0,listnumber,1)]
i=2
while(i<=50):
    for y in range(i*2,listnumber,i):
        x[y]=False
    i+=1
for z in range(2,listnumber):
    if(x[z]==True):
        print(z)


1,2,4,7,9,10,13,17,19,20,24