def bubble_sort(arr):
    """
        time complexity -> O(N^2)
        space complexity -> O(1)
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubble_sort([6, 2, 5, 1, 4, 9, 7, 8]))
