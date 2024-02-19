from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if v > 0:
                break

            if i > 0 and v == nums[i - 1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                three_sum = v + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
