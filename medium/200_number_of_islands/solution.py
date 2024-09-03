import collections
from typing import List

class Solution:
    """
    BFS solution
    starting from top left coner, bfs all the connected 1s layer by layer radiating outwards
    BFS mainly to fill the visit set
    """
    def bfs(self, r, c):
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
                    self.grid[r][c] == "1" and
                    (r, c) not in self.visit):
                    q.append((r,c))
                    self.visit.add((r,c))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not self.grid:
            return 0

        self.rows, self.cols = len(grid), len(grid[0])
        self.visit = set()
        self.islands = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1" and (r,c) not in self.visit:
                    self.bfs(r,c)
                    self.islands += 1

        return self.islands
    
class NeetSolution:
    """
    DFS solution (recursive)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
