import numpy as np
array=np.array([[4,5,9,2],[6,5,3,1]])
Final=0
for i in range (array.shape[0]):
    x=array[i].mean()
    print(x)
    if Final==0:
        Final=x-Final
    else:
        Final=Final-x

print(Final)
