from collections import defaultdict
from typing import List

class Solution:
    """
    time complexity: O(N^2)
    space complexity: O(N^2)
    """
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def out_of_bounds(r, c):
            return (
                r < 0 or c < 0 or
                r == N or c == N
            )

        def dfs(r, c, label):
            if (out_of_bounds(r, c) or
            grid[r][c] != 1): # either water or visited
                return 0 
            grid[r][c] = label
            size = 1 # the extra land we flipped
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in nei:
                size += dfs(nr, nc, label)
            return size
        
        # precomp all island area
        size = defaultdict(int)
        label = 2 # label start from 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1
        
        def connect(r, c):
            """
            get connected area if we flip (r, c) into island
            """
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            visit = set()
            ans = 1
            for nr, nc in nei:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    ans += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return ans

        # 2. flip the water
        ans = 0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    ans = max(ans, connect(r, c))
        return ans