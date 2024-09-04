from typing import List
import collections

class Solution:
    """
    BFS solution
    """
    def bfs(self, r, c):
        area = 1 # current cell is counted
        q = collections.deque()
        self.visit.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(self.rows) and
                    c in range(self.cols) and
                    self.grid[r][c] == 1 and
                    (r, c) not in self.visit):
                    q.append((r,c))
                    self.visit.add((r,c))
                    area += 1

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        if not self.grid:
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.visit = set()
        self.result_arr = []

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and (r,c) not in self.visit:
                    area = self.bfs(r,c)
                    self.result_arr.append(area)

        return max(self.result_arr) if self.result_arr else 0