from typing import List

class Solution:
    """
    DFS solution
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