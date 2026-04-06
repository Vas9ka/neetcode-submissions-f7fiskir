class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = ans_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i] + curr_max, nums[i])
            ans_max = max(ans_max, curr_max)
        return ans_max