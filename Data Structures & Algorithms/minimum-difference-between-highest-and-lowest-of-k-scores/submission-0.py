class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1 2 3 3 5 6
        curr = nums[k - 1] - nums[0]
        ans = curr
        for i in range(k, len(nums)):
            curr = nums[i] - nums[i - k + 1]
            ans = min(curr, ans)
        
        return ans
