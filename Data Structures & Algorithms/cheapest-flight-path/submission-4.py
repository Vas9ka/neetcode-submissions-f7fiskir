import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        graph = defaultdict(list)

        for u,v, w in flights:
            graph[u].append((v,w))

        distances[src] = 0
        heap = [(0, src, 0)]
        seen = set()
        while heap:
            distance, node, stops = heapq.heappop(heap)
            seen.add(node)
            if  stops > k:
                continue
            
            for nei, w in graph[node]:
                if nei not in seen:
                    heapq.heappush(heap, (distance + w,nei , stops + 1))
                    distances[nei] = min(distances[nei], distance  + w)

        return distances[dst] if distances[dst] != float('inf') else -1