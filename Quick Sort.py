def partition(arr,si,ei):
    index = si
    for i in range(si,ei):
        if (arr[i] < arr[ei]):
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    arr[index], arr[ei] = arr[ei], arr[index]
    return index

def quickSort(arr,si,ei):
    if si < ei:
        pivot = partition(arr,si,ei)

        quickSort(arr,si,pivot-1)
        quickSort(arr,pivot+1,ei)



a = [21,4,5,2,5,7,9,23,51,77,90]
b = [6,3,9,5,2,8]
quickSort(a,0,len(a)-1)
print(a)