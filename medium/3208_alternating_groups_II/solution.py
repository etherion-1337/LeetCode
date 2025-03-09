from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        l = 0
        N = len(colors)

        for r in range(1, N + k - 1):
            if colors[r % N] == colors[(r - 1) % N]:
                l = r
            if r - l + 1 == k:
                ans += 1
                l += 1

        return ans