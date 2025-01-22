from collections import deque
from typing import List

class Solution:
    """
    BFS
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque() # (r, c)
        ans = [[-1] * COLS for r in range(ROWS)]
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                    visited.add((r, c))
                    q.append((r, c))

        # multisource BFS from all water
        while q:
            r, c = q.popleft()
            h = ans[r][c]

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbors:
                if (nr < 0 or nr == ROWS or
                    nc < 0 or nc == COLS or
                    (nr, nc) in visited):
                    continue
                q.append((nr, nc))
                visited.add((nr, nc))
                ans[nr][nc] = h + 1
            
        return ans