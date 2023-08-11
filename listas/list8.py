#Matriz

a=[[1,2,3],
   [4,5,6]]

b=[[-1,0],
   [0,1],
   [1,1]]

c=[[0,0],
   [0,0]]



f1=2
c1=3
f2=3
c2=2



for x in range(f1):
    for y in range(c2):
        for j in range(f2):
            c[x][y]=c[x][y] + a[x][j]*b[j][y]


for i in c:
    print(i)

