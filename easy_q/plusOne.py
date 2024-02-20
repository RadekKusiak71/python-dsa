from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1

        while pointer >= 0:
            reminder = (digits[pointer] + 1) % 10
            if reminder != 0:
                digits[pointer] = reminder
                break
            digits[pointer] = reminder
            pointer -= 1

        if reminder == 0:
            digits.insert(0, 1)

        return digits


# print(Solution().plusOne([1, 2, 3]))
# print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9]))
