f = open('Python.txt', 'r')
n=int(input("Enter a number "))
count=0
for line in f:
    if n>count:
      count+=1
      print("Line {}: {}".format(count,line.strip(), end = ''))
