class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = len(s) - 1
        count = 0
        while pointer >= 0:
            if s[pointer] != ' ':
                count += 1
            if count > 0 and s[pointer] == ' ':
                return count
            pointer -= 1
        return count


print(Solution().lengthOfLastWord('a'))
