class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid_row = (top + bot) // 2


            if matrix[mid_row][0] > target:
                bot = mid_row - 1

            elif matrix[mid_row][-1] < target:
                top = mid_row + 1
            else:
                break
        if not (top <= bot):
            return False

        left_col = 0
        right_col = len(matrix[0]) - 1
        mid_row = (top + bot) // 2
        while left_col <=  right_col:
            mid_col = (left_col + right_col) // 2
            
            if matrix[mid_row][mid_col] == target:
                return True
            
            if matrix[mid_row][mid_col] > target:
                right_col = mid_col -1
            else:
                left_col = mid_col + 1
            
        return False

