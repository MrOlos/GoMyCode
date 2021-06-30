def takeSecond(elem):
    return elem[1]
tuple1= ('item1', '12.20')
tuple2=('item2', '15.10')
tuple3=('item3', '24.5')

list=[tuple2,tuple1,tuple3]

list.sort(key=takeSecond,reverse=True)

print(list)
