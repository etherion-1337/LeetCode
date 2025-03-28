from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()

        min_heap = [(grid[0][0], 0, 0)] # val, r, c
        ans = [0] * len(queries)
        visit = set([(0, 0)])
        points = 0

        for limit, idx in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1
                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for nr, nc in neighbors:
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit):
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visit.add((nr, nc))
            ans[idx] = points

        return ans