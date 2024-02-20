class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                pointer = 0
                while pointer <= len(needle)-1 and haystack[pointer+i] == needle[pointer]:
                    pointer += 1
                if pointer == len(needle):
                    return i
        return -1


print(Solution().strStr(haystack="sadbutsad", needle="sad"))
