class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        res = nums[0]
        right = len(nums) -1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            
        
        return res