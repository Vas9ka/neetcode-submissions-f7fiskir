class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if not nums:
            return 0
        def dp(i):
            if i <= 0:
                return nums[0]
            if i == 1:
                return max(nums[1], nums[0])
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        max_first = dp(len(nums) - 2)
        nums = nums[1:]
        if nums:
            memo = {}
            max_second = dp(len(nums) - 1)
            return max(max_first, max_second)
        return max_first

