from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            if arr[i] < temp:
                max_right = temp
        return arr


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
# RES - > [18,6,6,6,1,-1]
