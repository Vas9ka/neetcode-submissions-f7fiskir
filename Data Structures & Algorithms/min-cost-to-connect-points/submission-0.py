from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        seen = set()
        min_h = [(0,0)]
        total_cost = 0
        while len(seen) < n:
            cost, node = heapq.heappop(min_h)
            if node in seen:
                continue
            seen.add(node)
            total_cost += cost
            for nei_cost, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(min_h, (nei_cost, nei))
        
        return total_cost
