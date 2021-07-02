NumberElements=int(input("How many elements to sort? "))
Final=[]
for i in range(NumberElements):
    Element=str(input("Enter a word "))
    Final.append(Element)

Final.sort()
print('Sorted list:', Final)
