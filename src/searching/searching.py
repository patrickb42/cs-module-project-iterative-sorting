def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr, target):
    lower = 0
    upper = len(arr)
    if upper == 0:
        return -1
    while lower <= upper:
        middle = (upper - lower) // 2 + lower
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            upper = middle - 1
        else:
            lower = middle + 1
    return -1
