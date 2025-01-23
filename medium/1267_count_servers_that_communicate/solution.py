from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt = [0] * COLS
        col_cnt = [0] * ROWS
        ans = 0
        # pre-process
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_cnt[c] += 1
                    col_cnt[r] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if row_cnt[c] > 1 or col_cnt[r] > 1:
                        ans += 1

        return ans