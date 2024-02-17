def insertion_sort(arr):
    """
        time complexity -> O(N^2)
        space complexity -> O(1)
    """
    for i in range(len(arr)-1):
        while i >= 0 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i -= 1
    return arr


print(insertion_sort([6, 2, 5, 1, 4, 9, 7, 8]))
