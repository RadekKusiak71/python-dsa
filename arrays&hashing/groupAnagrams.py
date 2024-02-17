from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c)-97] += 1
            res[tuple(counter)].append(s)
        return res.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
