from collections import deque
from typing import List

class Solution:
    """
    0/1 bfs
    """
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1 : [0, 1],
            2 : [0, -1],
            3 : [1, 0],
            4 : [-1, 0]
        }

        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)]) # r, c, cost
        # the cost in triplet in q is not guaranteed to be smallest, it is just immediate cost
        # there could be other route that reach the same (r, c) with smaller cost
        # so need a hashmap to keep track
        min_cost = {
            (0, 0) : 0 # (r, c) : cost
        }
 
        while q:
            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS -1):
                return cost

            for d in directions:
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or n_cost >= min_cost.get((nr, nc), float("inf")):
                    continue
                
                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))