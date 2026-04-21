from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = defaultdict(list)
        in_degrees = [0] * n
        excluded = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degrees[v] += 1
            in_degrees[u] += 1
        
        q = deque()
        for i in range(len(in_degrees)):
            if in_degrees[i] == 1:
                q.append(i)
                excluded.add(i)

        remaining = n
        while remaining > 2:
            size = len(q)
            remaining -= size
            for _ in range(size):
                leaf = q.popleft()
                for nei in graph[leaf]:
                    in_degrees[nei] -= 1
                    if in_degrees[nei] == 1:
                        q.append(nei)
        return list(q)
        
