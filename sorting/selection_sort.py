def selection_sort(arr):
    """
        time complexity -> O(N^2)
        space complexity -> O(1)
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort([6, 2, 5, 1, 4, 9, 7, 8]))
