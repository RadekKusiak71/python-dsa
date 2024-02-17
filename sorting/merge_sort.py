def merge_sort(arr):
    """
        time complexity -> O(n*log(n))
        space complexity -> O(n)
    """
    if len(arr) > 1:
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge(arr, left_array, right_array)
    return arr


def merge(arr, left_arr, right_arr):
    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr


print(merge_sort([9, 6, 2, 4, 1, 3, 8, 7, 5]))
