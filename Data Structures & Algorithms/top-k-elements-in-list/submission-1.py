from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = Counter(nums)
        freqs = []
        for num, freq in nums_counts.items():
            pair = (freq, num)
            heapq.heappush(freqs, pair)
            if len(freqs) > k:
                heapq.heappop(freqs)
        return [num for _, num in freqs]