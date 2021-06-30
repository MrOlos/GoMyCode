n=input("type a string ")
a=""
for i in range(len(n)):
    if i%2==0:
        a=a+n[i]
        print(a)
