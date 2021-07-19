def mergeSort(List):
    if len(List) > 1:
        mid = len(List) // 2
        left = List[:mid]
        right = List[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              List[k] = left[i]
              i += 1
            else:
                List[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            List[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            List[k]=right[j]
            j += 1
            k += 1

sequence = [9,89,12,4,63,14,7,20,8,75,23,46]
mergeSort(sequence)
print(sequence)
