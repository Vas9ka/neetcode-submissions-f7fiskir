class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left  = 0
        for right in range(1, len(nums)):
            if nums[right] == nums[left] and left != right:
                return True
                
            while right - left + 1 > k and left < right:
                left += 1
                
            if nums[right] == nums[left] and left != right:
                return True


        return False