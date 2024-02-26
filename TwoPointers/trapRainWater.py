from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]]
        max_right = []
        ans = 0
        for i in range(1, len(height)):
            max_left.append(max(height[:i]))
            max_right.append(max(height[i:]))
        max_right.append(0)

        for i in range(len(height)):
            value = min(max_left[i], max_right[i]) - height[i]
            if value > 0:
                ans += value
        return ans


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
