from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_valid(row, col, val):
            return 0 <= row < n and 0 <= col < m and heights[row][col] >= val
        
        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if is_valid(nr, nc, heights[r][c]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        n = len(heights)
        m = len(heights[0])
        ans = []
        pacific_nodes = []
        atlantic_nodes = []
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        for i in range(n):  # rows
            pacific_nodes.append((i, 0))      # left column
            atlantic_nodes.append((i, m-1))   # right column

        for j in range(m):  # columns
            pacific_nodes.append((0, j))      # top row
            atlantic_nodes.append((n-1, j))   # bottom row

        pac = bfs(pacific_nodes)
        atl = bfs(atlantic_nodes)

        return [[r, c] for (r, c) in pac & atl]
