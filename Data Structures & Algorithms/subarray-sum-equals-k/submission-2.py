from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        ans = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in prefix_sum:
                ans += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1
            
        return ans


