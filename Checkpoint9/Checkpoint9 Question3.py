def bubbleSort(sequence):
    for passnum in range(len(sequence)-1,0,-1):
        for i in range(passnum):
            if sequence[i]>sequence[i+1]:
                temp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = temp
    return sequence

sort=bubbleSort([5,3,8,4,6,7,1,9,0,4])
print(sort)
