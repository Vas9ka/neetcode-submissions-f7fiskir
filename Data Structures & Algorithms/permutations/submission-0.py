class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        pick = [False] * len(nums)
        def backtrack(curr, path):
            if len(path) == len(nums):
                ans.append(path[:])
            
            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    backtrack(nums[i], path)
                    path.pop()
                    pick[i] = False
        backtrack(None, [])
        return ans