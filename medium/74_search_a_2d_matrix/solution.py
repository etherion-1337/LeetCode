from typing import List

class Solution:
    """
    Binary search on the concatenated list of the matrix
    time complexity: O(log(m*n))
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        concat_list = [elem for sublist in matrix for elem in sublist]

        ans = self.binary_search(concat_list, target)

        return ans

    def binary_search(self, arr: List, target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
        return False

class Solution:
    """
    2D Binary search on the matrix
    time complexity: O(log(m) + log(n))
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top = 0
        bottom = ROW - 1

        while top <= bottom:
            row = (top + bottom)//2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        if not top <= bottom:
            return False

        l = 0
        r = COL - 1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
    
class NeetSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False