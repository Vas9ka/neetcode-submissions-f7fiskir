class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for start, end in intervals:
            if ans and ans[-1][1] >= start:
                new_end = max(end, ans[-1][1])
                ans[-1][1] = new_end
            else:
                ans.append([start, end])
        
        return ans