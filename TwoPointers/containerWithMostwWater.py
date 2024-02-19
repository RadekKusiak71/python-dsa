from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_len = 0

        while left < right:
            if height[left] < height[right]:
                if height[left]*(right-left) > max_len:
                    max_len = height[left]*(right-left)
                left += 1
            else:
                if height[right]*(right-left) > max_len:
                    max_len = height[right]*(right-left)
                right -= 1
        return max_len


print(Solution().maxArea(height=[1, 2]))
