from typing import List

class Solution:
    """
    DFS solution
    check the cell at the 4 edges of the board and if it is "O" then do a dfs from that cell
    we change all "O" cells that can connect to theses edge "O" cells to "T"
    At the end we change all "O" cells to "X" and all "T" cells to "O" since those "T" (originally "O") cells are not surrounded by "X"

    time complexity: O(n*m)
    """
    def dfs(self, r, c):
        if r < 0 or r == self.ROWS or c < 0 or c == self.COLS or self.board[r][c] != "O":
            return

        self.board[r][c] = "T"
        self.dfs(r + 1, c)
        self.dfs(r - 1, c)
        self.dfs(r, c + 1)
        self.dfs(r, c - 1)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        # capture unsurrounded regions: O -> T on the 4 edges
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if r == 0 or r == self.ROWS -1 or c == 0 or c == self.COLS - 1:
                    if self.board[r][c] == "O":
                        self.dfs(r, c)

        # capture surrounded regions: O -> X
        # restore unsurrounded regions: T -> O
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.board[r][c] == "O":
                    self.board[r][c] = "X"
                elif self.board[r][c] == "T":
                    self.board[r][c] = "O"

        return self.board
    
class NeetSolution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

    