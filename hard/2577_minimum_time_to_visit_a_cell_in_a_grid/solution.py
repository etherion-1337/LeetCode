from typing import List
import heapq

class Solution:
    """
    variations of Dijkstra's algorithm

    time: O(m*n*log(m*n))
    space: O(m*n)
    """
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        # t, r, c
        min_heap = [(0, 0, 0)]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == ROWS - 1 and c == COLS - 1:
                return t

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited:
                    continue
                # if current cell and next cell have different parity, we need to wait
                if abs(grid[nr][nc] - t) % 2: # e.g. 3 -> 4, no need to wait
                    wait = 0
                else:
                    wait = 1 # e.g. 3 -> 5, need to go other cells then back, so its 6 when it actually arrives (nr, nc), i.e. waited 1 time unit
                # for edge case when we going from high number -> low number, we cannot turn back time
                next_time = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(min_heap, (next_time, nr, nc))
                visited.add((nr, nc))