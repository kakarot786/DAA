def selectionSort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i] , arr[smallest] = arr[smallest], arr[i]   # Swapping
    return arr



a = [1,3,7,8,0,2,4,9]
print(selectionSort(a))