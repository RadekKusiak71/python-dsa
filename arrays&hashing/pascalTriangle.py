from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            row = [1] * i
            left, right = 1, len(row) - 2
            while left <= right:
                row[left] = triangle[i - 2][left - 1] + triangle[i - 2][left]
                row[right] = triangle[i - 2][right - 1] + triangle[i - 2][right]
                left += 1
                right -= 1
            triangle.append(row)
        return triangle


print(Solution().generate(5))
