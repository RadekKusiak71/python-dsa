from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if nums[i] in res:
                return [res[nums[i]], i]
            res[value] = i


print(Solution().twoSum([2, 7, 11, 15], 9))
