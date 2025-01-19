from heapq import heappush, heappop
from typing import List

class Solution:
    """
    BFS solution with min heap
    """
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        # add border to min heap, mark as visited
        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        # priortise smallest height
        # maintain max height so far to get water stored in each inner position
        ans = 0
        max_h = -1

        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            # this is the hard part
            # intuition: we are going level by level (lowest to highest)
            # when we added a lower cell into the heap, we know that the water
            # we can store in the current cell is bounded by the max height so far
            # this max height is designed to be the lowest height of the surrounding cells (due to the way we use min heap)
            ans += max_h - h
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            
            for nr, nc in neighbors:
                if (
                    nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    heightMap[nr][nc] == -1
                ):
                    continue
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return ans