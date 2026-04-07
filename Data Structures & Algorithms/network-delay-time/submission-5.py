from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        distances[0] = 0
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        heap = [(0, k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue
            for nei, w in graph[node]:
                curr_delay = dist + w
                if curr_delay < distances[nei]:
                    distances[nei] = curr_delay
                    heapq.heappush(heap, (curr_delay, nei))
        
        return max(distances) if max(distances) != float('inf') else -1
