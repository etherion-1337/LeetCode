from typing import List

class Solution:
    def dfs(self, r, c, i):
        """
        r: row index
        c: col index
        i: word index
        """
        # we have reached beyond the end of word
        # previous char search all found
        if i == len(self.word):
            return True
        if (r < 0 or c < 0 or # out of bound of the board
            r >= self.ROWS or c >= self.COLS or # out of bound of the board
            self.word[i] != self.board[r][c] or # the current tile in the board is not we want
            (r, c) in self.path): # the current tile is visited previously
            return False
        
        self.path.add((r, c))
        # we looking for the next char hence i + 1
        # for each step, we look at 4 dir, each dir will then branch out to next 4 dir
        result = (self.dfs(r + 1, c, i + 1) or
                  self.dfs(r - 1, c, i + 1) or
                  self.dfs(r, c + 1, i + 1) or
                  self.dfs(r, c - 1, i + 1))
        self.path.remove((r, c))
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS solution
        time complexity: O(N * 4^L) where N is the number of cells in the board and L is the length of the word
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        self.word = word
        self.path = set()
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.dfs(r, c, 0):
                    return True
        
        return False