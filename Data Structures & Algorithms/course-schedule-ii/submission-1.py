from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        queue = deque()
        ans = []
        for v, u in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return ans if len(ans) == numCourses else []