def radixSort(arr):
    k = max(arr)
    pos = 1
    while (k/pos) > 0:
        arr = countSort(arr,pos)
        pos *= 10

    return arr


def countSort(arr,pos):
    n = len(arr)
    count = [0 for i in range(10)]
    sorted_arr = [0 for i in range(n)]
    for i in range(n):
        count[int(arr[i] / pos) % 10] += 1
    for i in range(1,len(count)):
        count[i] = count[i-1] + count[i]
    for i in range(n-1,0,-1):
        count[int(arr[i] / pos) % 10] -= 1
        sorted_arr[count[int(arr[i] / pos) % 10]] = arr[i]

    return sorted_arr


array = [432,8,530,90,88,231,11,45,677,199]
print(radixSort(array))