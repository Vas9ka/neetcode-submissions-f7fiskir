from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 1
        

        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        fresh_fruits = 0
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruits += 1
        if fresh_fruits == 0:
            return 0
        minutes = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dx, dy in directions:
                    new_row, new_col =  row + dx, col + dy
                    if is_valid(new_row, new_col):
                        fresh_fruits -= 1
                        if fresh_fruits == 0:
                            return minutes
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            minutes += 1
        return -1