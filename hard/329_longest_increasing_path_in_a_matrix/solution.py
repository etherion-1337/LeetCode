from typing import List

class Solution:
    """
    DFS with backtracking
    TLE
    """
    def dfs(self, r, c, prev_val):
        if (r < 0 or c < 0 or # out of bound of the room
            r >= self.ROWS or c >= self.COLS or # out of bound of the room
            self.matrix[r][c] <= prev_val or # smaller val
            (r, c) in self.path): # already visited
            self.tmp_result = max(self.tmp_result, len(self.path))
            return

        self.path.add((r, c))
        self.dfs(r + 1, c, self.matrix[r][c])
        self.dfs(r - 1, c, self.matrix[r][c])
        self.dfs(r, c + 1, self.matrix[r][c])
        self.dfs(r, c - 1, self.matrix[r][c])
        self.path.remove((r, c))
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.matrix = matrix
        self.result = []

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.tmp_result = 0
                self.path = set()
                # prev_val = -1 to handle cell with 0
                self.dfs(r, c, -1)
                self.result.append(self.tmp_result)

        return max(self.result)
    
class NeetSolution:
    """
    2D DP with memoization

    time complexity: O(m*n)
    space complexity: O(m*n)
    """
    def dfs(self, r, c, prev_val):
        if r < 0 or r >= self.ROWS or c < 0 or c >= self.COLS or self.matrix[r][c] <= prev_val:
            return 0
        if (r,c) in self.dp:
            return self.dp[(r,c)]
        # note that we no need maintain path since we enforce the order is increasing, a revisit or cyclic path is implicity excluded
        # base case, each cell's LIP will at least be 1
        result = 1
        result = max(result, 1 + self.dfs(r + 1, c, self.matrix[r][c]))
        result = max(result, 1 + self.dfs(r - 1, c, self.matrix[r][c]))
        result = max(result, 1 + self.dfs(r, c + 1, self.matrix[r][c]))
        result = max(result, 1 + self.dfs(r, c - 1, self.matrix[r][c]))
        self.dp[(r,c)] = result
        return result

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.matrix = matrix
        # key: (r, c)
        # val: LIP
        self.dp = {}

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, -1)

        return max(self.dp.values())