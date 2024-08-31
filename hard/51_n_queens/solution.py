from typing import List

class Solution:
    def dfs(self, r):
        """
        dfs search row by row
        use r + c and r - c to track diag in 2 direction (pos and neg)
        """
        # base case
        # if we hit here means we reached a valid pattern
        if r == self.n:
            # comform to the submission format
            _tmp = ["".join(row) for row in self.board]
            self.result.append(_tmp)
            return

        # at current row, try put Q in each position (cols)
        # from there we dfs down each row
        for c in range(self.n):
            if c in self.col or (r + c) in self.posDiag or (r - c) in self.negDiag:
                continue
            
            # update track
            self.col.add(c)
            self.posDiag.add(r + c)
            self.negDiag.add(r - c)
            self.board[r][c] = "Q"

            self.dfs(r + 1)

            # clean up track
            self.col.remove(c)
            self.posDiag.remove(r + c)
            self.negDiag.remove(r - c)
            self.board[r][c] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result = []
        # n x n board
        self.board = [["."]*n for i in range(n)]
        # these 3 sets are sufficent to determine board patterns
        self.col = set()
        self.posDiag = set() # (r + c) is constant for each diag line
        self.negDiag = set() # (r - c) is constant for each diag line

        self.dfs(0)

        return self.result
    
class NeetSolution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
