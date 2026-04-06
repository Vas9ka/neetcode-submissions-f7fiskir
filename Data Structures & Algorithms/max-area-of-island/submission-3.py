class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 1
        
        def dfs(row, col):
            stack = [(row, col)]
            grid[row][col] = 0
            area = 1
            while stack:
                row, col = stack.pop()
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy
                    if is_valid(new_row, new_col):
                        area += 1
                        grid[new_row][new_col] = 0
                        stack.append((new_row, new_col))
            return area
        
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        max_area = 0
        for i in range(n):
            for j in range(m):
                if is_valid(i, j):
                    max_area = max(max_area, dfs(i, j))
        return max_area
                    