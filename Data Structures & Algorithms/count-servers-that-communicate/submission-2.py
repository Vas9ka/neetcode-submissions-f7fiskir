class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        row_count = [0] * n
        col_count = [0] * m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    ans += 1
        
        return ans