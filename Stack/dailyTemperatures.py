from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                val = stack.pop(-1)
                days[val[1]] = i - val[1]
            stack.append((t, i))
        return days


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
