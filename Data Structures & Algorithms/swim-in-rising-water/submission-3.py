import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        w_level = grid[0][0]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < n 

        seen = set()
        heap = [(grid[0][0], 0, 0)] 

        while heap:
            height, row, col = heapq.heappop(heap)
            if (row, col) in seen:
                continue
            seen.add((row, col))
            if row == n - 1 and col == n - 1:
                return height
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    heapq.heappush(heap, (max(height, grid[new_row][new_col]), new_row, new_col))
