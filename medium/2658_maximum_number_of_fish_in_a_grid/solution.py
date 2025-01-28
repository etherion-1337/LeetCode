from typing import List

class Solution:
    """
    DFS
    """
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS
                or grid[r][c] == 0 or (r, c) in visited):
                return 0
                
            visited.add((r, c))
            result = grid[r][c]
            neighbors = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
            for nr, nc in neighbors:
                result += dfs(nr, nc)

            return result


        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c))

        return ans