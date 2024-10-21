from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        time complexity: O(n^2)
        space complexity: O(1)
        use the top left corner as a tmp variable to store the value of the top left corner
        actual processing order is from top left anti-clockwise
        """
        # left and right boundary of the current sq
        l, r = 0, len(matrix) - 1
        while l < r: # we are closing in, make sure they dun cross
            for i in range(r - l):
                # top and bottom boundary of the current sq
                top, bottom = l, r
                # save the topleft to tmp
                top_left = matrix[top][l + i]
                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left to top right
                matrix[top +i][r] = top_left
            r -= 1
            l += 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        transpose the matrix and then reverse each row
        """
        #transpose 
        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        #reverse
        for row in matrix:
            row.reverse()