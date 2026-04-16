class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        
        def backtrack(start, path):
            prev = None
            for i in range(start, len(nums)):
                if nums[i] != prev:
                    path.append(nums[i])
                    ans.append(path[:])
                    backtrack(i + 1, path)
                    path.pop()
                    prev = nums[i]
        
        backtrack(0, [])
        return ans