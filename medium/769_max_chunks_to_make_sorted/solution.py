from typing import List

class Solution:
    """
    greedy approach
    """
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        res = 0
        # the max value has to appear at the index of the max value for the chunk to be sorted
        # since there is no duplicate, if the max value is at the index of the max value, then all the values before it are smaller
        # if it were to have bigger values before it, then the max value would have been bigger
        for i, n in enumerate(arr):
            curr_max = max(n, curr_max)

            if curr_max == i:
                res += 1

        return res