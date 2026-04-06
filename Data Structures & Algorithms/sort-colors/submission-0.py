class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indexes = [0, 0, 0]
        for i in range(len(nums)):
            indexes[nums[i]] += 1
        index = 0
        to_modify = 0
        while index < len(indexes):
            for i in range(indexes[index]): 
                nums[to_modify] = index 
                to_modify += 1
            index += 1
        
       