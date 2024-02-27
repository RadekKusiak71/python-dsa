from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = nums.count(val)
        for i in range(x):
            nums.remove(val)


Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
