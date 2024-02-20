def binarySearch(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        m = (left+right)//2
        if nums[m] == target:
            return m
        if nums[m] > target:
            right = m-1
        else:
            left = m+1
    return - 1


print(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
