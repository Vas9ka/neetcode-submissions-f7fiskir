"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x.start)
        heapq.heappush(heap, intervals[0].end)
        curr = ans = 1

        for interval in intervals[1:]:
            if heap[0] > interval.start:
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)

        return len(heap)