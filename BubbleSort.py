def bubbleSort(arr):
    for i in range(len(arr)):
        flag = True
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                flag = False
        if flag:
            return arr
    return arr


a = [20, 30, 89, 11, 23, 69, 75]
print(bubbleSort(a))
