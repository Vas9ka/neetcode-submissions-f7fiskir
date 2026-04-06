class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (1,0), (-1, 0), (0, -1)]
        def is_valid(row, col):
            return 0 <= row < n and 0 <= col < m and board[row][col] == 'O'


        def dfs(row, col):
            board[row][col] = '#'
            for dx, dy in directions:
                if is_valid(row + dx, col + dy):
                    dfs(row + dx, col + dy)
        


        for i in range(n):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][m - 1] == 'O': dfs(i, m - 1)
        
        for j in range(m):
            if board[0][j] == 'O': dfs(0, j)
            if board[n-1][j] == 'O': dfs(n - 1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        