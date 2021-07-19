def binary_search(sequence, item):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if sequence[mid] < item:
            low = mid + 1
        elif sequence[mid] > item:
            high = mid - 1
        else:
            return mid
    return False

arr = [ 2, 3, 5, 10, 40 ]
x = 5
result = binary_search(arr, x)
print(result)
