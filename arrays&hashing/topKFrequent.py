import heapq
import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = collections.defaultdict(int)

        for n in nums:
            counter[n] += 1

        min_heap = []
        for val, freq in counter.items():
            heapq.heappush(min_heap, (freq, val))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [f[1] for f in min_heap]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], k=2))
