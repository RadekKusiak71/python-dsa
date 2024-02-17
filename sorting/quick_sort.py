def quick_sort(arr, start, end):
    """
        time complexity -> O(n*log(n))
        space complexity -> O(log(n))
    """
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


arr = [7, 6, 9, 4, 2, 1, 5, 3, 8]


print(quick_sort(arr, 0, len(arr)-1))
