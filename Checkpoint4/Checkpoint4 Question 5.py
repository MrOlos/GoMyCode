import numpy as np
L1=[4,5,10,2,6,15,25]
listeeven=[]
listeodd=[]
def multiple(L):
    nL=np.prod(L)
    print(nL)

def sum1(L):
    nL=sum(L)
    print(nL)

for i in range (len(L1)):
    if i%2==0:
        listeeven.append(L1[i])
    else:
        listeodd.append(L1[i])
multiple(listeodd)
sum1(listeeven)
