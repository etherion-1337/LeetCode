from typing import List

class Solution:
    """
    DFS solution

    time complexity: O(m*n)^2, where m is the number of rows and n is the number of columns
    """
    def dfs(self, r, c, prev_h):
        # avoid TLE
        if "P" in self._tmp and "A" in self._tmp:
            return
        # if within bounds, and the height is greater than the previous height, then stop
        if r >= 0 and c >= 0 and r < self.ROWS and c < self.COLS:
            if self.heights[r][c] > prev_h or (r,c) in self.visited:
                return
        if r < 0 or c < 0:
            self._tmp.append("P") # can reach pacific
            return
        if r >= self.ROWS or c >= self.COLS:
            self._tmp.append("A") # can reach atlantic
            return

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            self.visited.add((r,c)) # each cell start its own visited set
            self.dfs(r + dr, c + dc, self.heights[r][c])
            self.visited.remove((r,c))


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(heights)
        self.COLS = len(heights[0])
        self.ans = []
        self.heights = heights
        self.visited = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self._tmp = []
                self.dfs(r,c, self.heights[r][c])
                if "P" in self._tmp and "A" in self._tmp:
                    self.ans.append([r,c])

        return self.ans
    
class NeetSolution:
    """
    DFS solution
    But from the 4 edges of the island back trace towards inside the island
    Then find the intersection of the two sets
    Or we can just check if the cell is in both sets

    time complexity: O(m*n), where m is the number of rows and n is the number of columns
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = atl.intersection(pac)
        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        return list(res)