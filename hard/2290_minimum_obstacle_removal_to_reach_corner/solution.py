import heapq
from typing import List

class Solution:
    """
    variant of Dijkstra's algorithm
    """
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cost_grid = [[float("inf")] * COLS for r in range(ROWS)]

        min_heap = []
        # (cost, r, c), cost is number of obstacle needs to be removed
        heapq.heappush(min_heap, (0, 0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while min_heap:
            cost, r, c = heapq.heappop(min_heap)

            if cost > cost_grid[r][c]:
                continue
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS:
                    continue
                new_cost = cost # need to define this since 4-dir for loop will reuse the variable cost
                if grid[new_r][new_c] == 1:
                    new_cost = cost + 1
                if cost_grid[new_r][new_c] > new_cost:
                    cost_grid[new_r][new_c] = new_cost
                    heapq.heappush(min_heap, (new_cost, new_r, new_c))

        return cost_grid[ROWS - 1][COLS - 1]