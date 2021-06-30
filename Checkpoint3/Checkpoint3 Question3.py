from collections import Counter
dict1={'a':100,'b':200,'c':200}
dict2={'a':300,'b':200,'d':400}
d = Counter(dict1) + Counter(dict2)
print(d)
