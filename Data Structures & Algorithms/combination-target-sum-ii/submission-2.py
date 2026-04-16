class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(path, curr_sum, start):
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(path[:])
            prev = None
            for i in range(start, len(candidates)):
                    if candidates[i] != prev:
                        path.append(candidates[i])
                        curr_sum += candidates[i]
                        backtrack(path, curr_sum, i + 1)
                        path.pop()
                        curr_sum -= candidates[i]
                        prev = candidates[i]
        
        backtrack([], 0, 0)
        return ans