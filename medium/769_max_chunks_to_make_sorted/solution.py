from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        res = 0

        for i, n in enumerate(arr):
            curr_max = max(n, curr_max)

            if curr_max == i:
                res += 1

        return res