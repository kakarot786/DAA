def maxHeap(arr):
    heapsize = len(arr)
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, heapsize)


def heapify(arr, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < heapsize and arr[l] > arr[largest]:
        largest = l
    if r < heapsize and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heapsize)


def heapSort(arr):
    heapsize = len(arr)
    maxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapsize -= 1
        heapify(arr, 0, heapsize)


a = [1, 5, 90, 8, 12, 14, 16]
heapSort(a)
print(a)
