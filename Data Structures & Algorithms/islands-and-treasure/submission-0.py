from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == INF
        
        n = len(grid)
        m = len(grid[0])
        seen = set()
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen.add((i, j))
                    queue.append((i, j))
        dst = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy
                    if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                        grid[new_row][new_col] = dst
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))
            dst += 1
        return 