class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start, curr_sum, path):
            if curr_sum == target:
                ans.append(path[:])
            if curr_sum > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                curr_sum += nums[i]

                backtrack(i, curr_sum, path)
                path.pop()
                curr_sum -= nums[i]
        

        backtrack(0, 0, [])
        return ans
