import numpy
List=[5,4,9,12]

ListEven=[]
ListOdd=[]
def Multiply(L):
    print(numpy.prod(L))
def Sum(L):
    print(sum(L))

for i in range(len(List)):
    if(i%2==0):
        ListEven.append(List[i])
    else:
        ListOdd.append(List[i])

Sum(ListEven)
Multiply(ListOdd)
