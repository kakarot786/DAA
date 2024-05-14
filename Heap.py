def maxHeap(arr):
    for i in range(len(arr) // 2, 1, -1):
        heapify(arr, i)


def heapify(arr, i):
    l = 2 * i   # Left node
    r = (2*i) + 1   # Right Node
    if l<len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r <= len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i] , arr[largest] = arr[largest], arr[i]
    heapify(arr,largest)



