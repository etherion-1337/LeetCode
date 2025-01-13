from typing import List

class NumMatrix:
    """
    prefix sum

    time complexity: O(m * n) for __init__, O(1) for sumRegion
    space complexity: O(m * n) for __init__, O(1) for sumRegion
    """
    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.board = [[0] * (self.COLS + 1) for r in range(self.ROWS + 1)]

        for r in range(self.ROWS):
            prefix = 0
            for c in range(self.COLS):
                prefix += matrix[r][c] 
                above = self.board[r][c + 1] # r + 1 - 1, remember it is offset by 1
                self.board[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        bottom_right = self.board[r2][c2]
        above = self.board[r1 - 1][c2]
        left = self.board[r2][c1 - 1]
        top_left = self.board[r1 - 1][c1 - 1] # make up for double count

        return bottom_right - above - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)