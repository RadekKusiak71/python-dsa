class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        vals = [1] * len(nums)

        for i in range(1, len(nums)):
            vals[i] = nums[i-1] * vals[i-1]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            vals[i] *= postfix
            postfix *= nums[i]
        return nums


print(Solution().productExceptSelf([1, 2, 3, 4]))
