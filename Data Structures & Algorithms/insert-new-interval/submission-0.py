class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx,interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[idx:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                new_start = min(interval[0], newInterval[0])
                new_end = max(interval[1], newInterval[1])
                newInterval = [new_start, new_end]

        res.append(newInterval)
        return res