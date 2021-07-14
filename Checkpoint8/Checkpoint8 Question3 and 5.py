f = open('Python.txt', 'r')
f1=f.readlines()
n=int(input("Enter a number "))
count=8
for line in f1[-n:]:
    if n>0:
      count+=1
      print("Line {}: {}".format(count-n,line.strip(), end = ''))
