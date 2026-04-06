from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = Counter(nums)
        keys = [k for k, _ in sorted(nums_counts.items(), key=lambda x: -x[1])]
        return keys[:k]