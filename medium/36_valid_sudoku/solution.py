from typing import List
from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for i in range(9):
            filled_row = [num for num in board[i] if num != "."]
            if len(filled_row) != len(set(filled_row)):
                return False

        # check col
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            filled_col = [num for num in col if num != "."]
            if len(filled_col) != len(set(filled_col)):
                return False

        # check subbox
        box_corner = [[[0,2],[0,2]],[[3,5],[0,2]],[[6,8],[0,2]],[[0,2],[3,5]], [[3,5],[3,5]],[[6,8],[3,5]],[[0,2],[6,8]],[[3,5],[6,8]],[[6,8],[6,8]]]

        for box in box_corner:
            box_nums = []
            for i in range(box[0][0],box[0][1]+1):
                for j in range(box[1][0], box[1][1]+1):
                    box_nums.append(board[i][j])
            filled_box = [num for num in box_nums if num != "."]
            if len(filled_box) != len(set(filled_box)):
                return False
        
        return True
    
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        time complexity: O(9^2)
        space complexity: O(9^2)
        stored the filled numbers in each row, col, and box hashset
        for boxes, we use (r//3, c//3) as the key so that we reduce from 81*81 -> 3*3 grid to identify the box
        """
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(9): #row
            for c in range(9): #col
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in box_set[(r//3,c//3)]:
                    return False
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[(r//3,c//3)].add(board[r][c])
    
        return True
    
class NeetSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
