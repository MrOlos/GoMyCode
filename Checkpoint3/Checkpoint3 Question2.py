# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 5), (1, 2), (4, 4), (2, 3),(2,1)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
