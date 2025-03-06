from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid)
        ans = [-1, -1]
        nums = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in nums:
                    ans[0] = grid[r][c]
                else:
                    nums.add(grid[r][c])

        for n in range(1, ROWS*COLS+1):
            if n not in nums:
                ans[1] = n

        return ans
