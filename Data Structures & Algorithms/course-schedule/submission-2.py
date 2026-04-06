from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        q = deque()
        visited = 0


        for v, u in prerequisites: 
            in_degree[v] += 1
            graph[u].append(v)
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            visited += 1
            for nei in graph[u]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return visited == numCourses

