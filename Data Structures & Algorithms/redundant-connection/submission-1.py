from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degrees = [0] * (len(edges) + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degrees[u] += 1
            in_degrees[v] += 1

        q = deque()
        for i in range(1, len(edges) + 1):
            if in_degrees[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            in_degrees[node] -= 1
            for nei in graph[node]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 1:
                    q.append(nei)
        
        for u, v in edges[::-1]:
            if in_degrees[u] > 0 and in_degrees[v] > 0:
                return [u, v]
        