import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            first_max = heapq.heappop_max(stones)
            second_max = heapq.heappop_max(stones)
            if first_max > second_max:
                first_max -= second_max
                heapq.heappush_max(stones, first_max)
        
        return stones[0] if stones else 0