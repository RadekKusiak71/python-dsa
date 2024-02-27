from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for indx, temp in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][1] < temp:
                removed_temp = stack.pop(-1)
                days[removed_temp[0]] = indx - removed_temp[0]
            stack.append((indx, temp))
        return days


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [ 1 , 1, 4 , 2 , 1 , 1 , 0 , 0]
