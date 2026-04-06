class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) -1 or grid[i][j] == 0:
                return 1
            if (i, j) in seen:
                return 0
            
            seen.add((i, j))
            perim = 0
            for dx, dy in directions:
                perim += dfs(i + dx, j + dy)

            return perim
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

        return 0
