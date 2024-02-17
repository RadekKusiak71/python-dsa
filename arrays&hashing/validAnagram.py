class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = [0]*26
        T = [0]*26
        for i in range(len(s)):
            S[ord(s[i])-97] += 1
            T[ord(t[i])-97] += 1

        return S == T


print(Solution().isAnagram('anagram', 'nagaram'))
