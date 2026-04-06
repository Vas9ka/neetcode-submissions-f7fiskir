class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        best_len = float('inf')
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                best_len = min(best_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

            

            
        if best_len == float('inf'):
            return 0
    
        return best_len


