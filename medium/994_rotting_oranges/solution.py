from collections import deque
from typing import List

class Solution:
    """
    BFS solution from each rotten orange
    Similar to medium/286_walls_and_gates/solution.py
    Time complexity: O(mn)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))


        def addRotting(r,c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] == 0 or
                grid[r][c] == 2):
                return
            grid[r][c] = 2
            visited.add((r, c))
            q.append([r, c])

        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addRotting(r + 1, c)
                addRotting(r - 1, c)
                addRotting(r, c + 1)
                addRotting(r, c - 1)
            if q:
                time += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time