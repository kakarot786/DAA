def mergeSort(arr, si, ei):
    if si >= ei:
        return
    else:
        mid = (si + ei) // 2
        mergeSort(arr, si, mid)
        mergeSort(arr, mid + 1, ei)

        index1, index2, x = si, mid + 1, 0
        merged = []
        while index1 <= mid and index2 <= ei:
            if arr[index1] < arr[index2]:
                merged.append(arr[index1])
                index1 += 1
            else:
                merged.append(arr[index2])
                index2 += 1

        while index1 <= mid:
            merged.append(arr[index1])
            index1 += 1

        while index2 <= ei:
            merged.append(arr[index2])
            index2 += 1

        for i, j in zip(range(len(merged)), range(si, ei+1)):
            arr[j] = merged[i]


arr = [92, 12, 32, 15, 16, 2, 1,]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
