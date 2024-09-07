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
            grid[r][c] = 2 # make it rotten
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
            # increment time after each level
            # only if there are rotten oranges
            # else it will be incremented in the end (+ 1 extra)
            if q:
                time += 1
        # check if there are any fresh oranges left
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time
    
class NeetSolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1