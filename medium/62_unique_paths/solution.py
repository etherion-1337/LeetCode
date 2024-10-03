

class Solution:
    """
    DFS with backtracking solution
    TLE on LC
    """
    def dfs(self, r, c):
        if r == self.ROWS - 1 and c == self.COLS - 1:
            self.result += 1
            return
        if (r < 0 or c < 0 or # out of bound of the board
            r >= self.ROWS or c >= self.COLS or # out of bound of the board
            (r, c) in self.path): # the current tile is visited previously
            return
        
        self.path.add((r, c))
        self.dfs(r + 1, c)
        self.dfs(r, c + 1)
        self.path.remove((r, c))

    def uniquePaths(self, m: int, n: int) -> int:
        self.ROWS = m
        self.COLS = n
        self.path = set()
        self.result = 0

        self.dfs(0,0)

class Solution:
    """
    DFS with backtracking solution with cache
    """
    def dfs(self, r, c):
        # within bound (first) and then check if the board has a cached value
        # if there is a hit in cache, we return and this tile will not be visited again in this current run due to self.path
        if r >=0 and c >=0 and r < self.ROWS and c < self.COLS and self.board[r][c] != 0:
            self.tmp += self.board[r][c]
            return
        if r == self.ROWS - 1 and c == self.COLS - 1:
            self.tmp += 1
            return
        if (r < 0 or c < 0 or # out of bound of the board
            r >= self.ROWS or c >= self.COLS or # out of bound of the board
            (r, c) in self.path): # the current tile is visited previously
            return
        
        self.path.add((r, c))
        self.dfs(r + 1, c)
        self.dfs(r, c + 1)
        self.path.remove((r, c))

    def uniquePaths(self, m: int, n: int) -> int:
        # the board[r][c] cache the unique path from (r,c) to the destination
        self.board = [[0] * n for i in range(m)]
        self.ROWS = m
        self.COLS = n
        self.path = set()
        self.result = 0

        for r in range(self.ROWS - 1, -1, -1):
            for c in range(self.COLS - 1, -1, -1):
                self.tmp = 0
                self.dfs(r,c)
                self.board[r][c] = self.tmp
            
        return self.board[0][0]
    
class NeetSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        DP solution

        in the board, each cell stores the num of unique paths
        since it can only move down or right, the vale of the curr cell is the sum of right and down cell
        the most bottom row and the most right col is always 1, since only way to move to goal

        in implementation we need to keep track of 2 rows: compute the curr row and maintain the bottom (prev) row
        we start from the bottom row and start from the right most cell
        any out of bound cell has value of 0 and the goal cell has value of 1
        """
        # base case: most bottom row
        prev_row = [1] * n # n = cols

        # ignore the last row
        for i in range(m-1):
            curr_row = [1] * n
            # we igore the last col since it is always 1
            # also addresed out of bound
            for j in range(n-2, -1, -1):
                curr_row[j] = curr_row[j+1] + prev_row[j] # right + down
            prev_row = curr_row
        # return pre_row here because edge case of 1 row -> curr_row don't exist yet
        # since prev_row = curr_row it will be the same for other cases
        return prev_row[0]