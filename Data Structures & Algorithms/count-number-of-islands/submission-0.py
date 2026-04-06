class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == '1'
        


        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        start = (0, 0)
        n = len(grid)
        m = len(grid[0])
        seen = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in seen:
                    stack = [(i,j)]
                    seen.add((i, j))
                    ans += 1
                    while stack:
                        row, col = stack.pop()
                        for dx, dy in directions:
                            new_row = row + dx
                            new_col = col + dy
                            if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                                stack.append((new_row, new_col))
                                seen.add((new_row, new_col))
        return ans

