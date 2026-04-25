class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = nums[0]
        ans = max_prod
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(max_prod * nums[i], nums[i])
            min_prod = min(min_prod * nums[i], nums[i])
            ans = max(ans, max_prod)
        return ans