class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(min_sum):
            subarray = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > min_sum:
                    subarray += 1
                    curr_sum = num
            
            return subarray <= k
        
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l