from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            row_index = (l+r) // 2
            if matrix[row_index][0] > target:
                r = row_index - 1
            elif matrix[row_index][-1] < target:
                l = row_index + 1
            else:
                break

        l, r = 0, len(matrix[row_index])-1

        while l <= r:
            col = (l+r)//2
            if matrix[row_index][col] == target:
                return True
            if matrix[row_index][col] > target:
                r = col - 1
            if matrix[row_index][col] < target:
                l = col + 1
        return False


print(Solution().searchMatrix(
    matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]],
    target=3
))
