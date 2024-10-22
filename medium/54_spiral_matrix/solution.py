from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        the right and bottom boundary is set out of bound by 1 for easier calculation 
        """
        result = []
        top, bottom = 0, len(matrix) # out of bound by 1
        left, right = 0, len(matrix[0]) # out of bound by 1

        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # right col
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            
            # need to check in between else error
            # for edge case :col and row vector
            if not (left < right and top < bottom):
                break

            # bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # left col
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result