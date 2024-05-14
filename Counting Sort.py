def countingSort(arr):
    n = len(arr)
    k = max(arr)
    count = [0 for i in range(k+1)]
    sorted_arr = [0 for i in range(n)]
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1,k):
        count[i] = count[i-1] + count[i]
    for i in range(n-1,0,-1):
        count[arr[i]] -= 1
        sorted_arr[count[arr[i]]] = arr[i]

    return sorted_arr


a = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(countingSort(a))