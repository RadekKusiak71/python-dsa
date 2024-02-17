class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if self.skip(s[left]):
                left += 1
                continue
            if self.skip(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def skip(self, ch: chr):
        if (48 <= ord(ch) <= 57 or
            65 <= ord(ch) <= 90 or
                97 <= ord(ch) <= 122):
            return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
