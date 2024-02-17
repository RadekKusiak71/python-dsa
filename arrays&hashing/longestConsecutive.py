class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hset = set(nums)
        longest = 0
        for n in hset:
            length = 0
            if n-1 not in hset:
                length = 1
                while n + length in hset:
                    length += 1
            longest = max(longest, length)
        return longest


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
