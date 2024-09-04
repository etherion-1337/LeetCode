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
    
class Solution:
    """
    DFS solution (recursive)
    time and space complexity: O(m*n)
    """
    def dfs(self, r, c):
        if (
            r not in range(self.rows)
            or c not in range(self.cols)
            or self.grid[r][c] == 0
            or (r, c) in self.visit
        ):
            return

        self.area += 1
        self.visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            self.dfs(r + dr, c + dc)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid

        if not self.grid or not self.grid[0]:
            return 0

        area_list = []
        self.visit = set()
        self.rows, self.cols = len(grid), len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and (r, c) not in self.visit:
                    self.area = 0
                    self.dfs(r, c)
                    area_list.append(self.area)

        return max(area_list) if area_list else 0
    
class NeetSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area