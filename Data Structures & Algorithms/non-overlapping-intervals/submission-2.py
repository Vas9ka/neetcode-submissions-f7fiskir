class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if prev_end > start:
                ans += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return ans