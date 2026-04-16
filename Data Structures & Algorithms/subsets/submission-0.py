class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def backtrack(start, path):

            for i in range(start, len(nums)):
                path.append(nums[i])
                ans.append(path[:])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans
