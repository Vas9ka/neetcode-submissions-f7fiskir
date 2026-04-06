class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if len(nums) == 0:
            return 0
        ans = 1
        for num in seen:
            counter = 1
            start_seq = num - 1
            if start_seq in seen:
                while start_seq + counter in seen:
                    counter += 1
            ans = max(counter, ans)
        return ans
