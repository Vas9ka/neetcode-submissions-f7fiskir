from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        
        return ans