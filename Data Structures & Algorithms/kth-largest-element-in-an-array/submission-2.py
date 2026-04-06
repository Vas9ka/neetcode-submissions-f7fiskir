import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [nums[0]]
        ans = 0 
        for i in range(1, len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]