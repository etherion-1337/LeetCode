from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    ans = max(ans, length)

        return ans