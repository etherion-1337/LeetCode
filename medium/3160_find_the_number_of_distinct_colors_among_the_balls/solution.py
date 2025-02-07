from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        freq = defaultdict(lambda: 0) # color -> count
        colors = defaultdict(lambda: 0) # ball idx -> color, intially all is 0

        ans = []
        for x, y in queries:
            prev = colors[x]
            if prev != 0:
                freq[prev] -= 1
                if freq[prev] == 0:
                    del freq[prev]
            colors[x] = y
            freq[y] += 1
            ans.append(len(freq))

        return ans