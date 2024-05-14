def linearSearch(arr, element):
    i = 0
    while i < len(arr) and arr[i] != element:
        i += 1

    if arr[i] == element:
        return i
    else:
        return -1


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(linearSearch(a, 8))


# for i in range(len(arr)):
#     if arr[i] == element:
#         return i
# return -1


def binarySearch(arr, element, low, high):
    mid = int(low + high / 2)
    if arr[mid] == element:
        return mid
    else:
        if element > mid:
            return binarySearch(arr, element, mid + 1, high)
        else:
            return binarySearch(arr, element, low, mid - 1)


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = binarySearch(b, 7, 0, len(b) - 1)
print(c)
