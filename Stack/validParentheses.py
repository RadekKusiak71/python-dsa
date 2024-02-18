class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for c in s:
            if c not in chars:
                stack.append(c)
                continue
            if not stack or stack.pop() != chars[c]:
                return False
        if len(stack) == 0:
            return True
        return False
