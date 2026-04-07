from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        distances[0] = 0
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        q = deque([(k, 0)])
        while q:
            node, delay = q.popleft()
            for nei, w in graph[node]:
                curr_delay = delay + w
                if curr_delay < distances[nei]:
                    distances[nei] = curr_delay
                    q.append((nei, curr_delay))
        
        return max(distances) if max(distances) != float('inf') else -1
