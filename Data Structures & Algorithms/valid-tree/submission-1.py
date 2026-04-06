from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        graph = defaultdict(list)
        stack = [0]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        while stack:
            node = stack.pop()
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)
        
        return len(edges) == n - 1 and len(seen) == n