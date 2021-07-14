x=str(input("Enter file name "))
f=x+'.txt'
f1=open(f,"r",encoding='utf-8')
data=f1.read()
words = data.split()

print('Number of words in text file :', len(words))
