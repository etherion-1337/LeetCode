from typing import List

class Solution:
    def set_zero(self, r, c, matrix):
        """
        given a cell, change row and col to 0
        """
        # set row = 0
        for i in range(0, self.COLS):
            matrix[r][i] = 0
        # set col = 0
        for j in range(0, self.ROWS):
            matrix[j][c] = 0
        return matrix

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        time complexity: O(m*n)
        space complexity: O(m+n)
        """
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        candidate = set()

        # find all cell == 0
        # we cannot put set_zero here as it will mess up the answer
        for r in range(0, self.ROWS):
            for c in range(0, self.COLS):
                if matrix[r][c] == 0:
                    candidate.add((r,c))

        for r, c in candidate:
            matrix = self.set_zero(r, c, matrix)

class NeetSolution:
    """
    this is the O(1) space solution

    we just need to mark the row and col that need to be set to 0, but do it in place by using the first row and col as the marker
    the extra space comes from the rowZero variable which is the overlap of the first row and the first col
    that variable determines if the first row should be set to 0
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        # determine which row and col to set to 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True # dedicated first row marker
        # skip first row and col as they are the marker
        # we deal with them later
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # deal with first col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        # deal with first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0