from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prefix_row1, prefix_row2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            prefix_row1[i] += prefix_row1[i - 1]
            prefix_row2[i] += prefix_row2[i - 1]

        ans = float("inf")
        # 1st robot want to minimise 2nd robot score
        for i in range(N): # the idx where the 1st robot can jump to row 2
            top_row = prefix_row1[-1] - prefix_row1[i]
            bottom_row = prefix_row2[i - 1] if i > 0 else 0
            second_robot = max(top_row, bottom_row) # 2nd robot can only choose one path
            ans = min(ans, second_robot) # 1st robot minmize 2nd robot

        return ans