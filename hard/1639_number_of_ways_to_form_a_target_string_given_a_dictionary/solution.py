from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        # (index or k, char) -> count among all word in words
        count = defaultdict(int)
        for word in words:
            for i, char in enumerate(word):
                count[(i, char)] += 1
        # (i, k) -> num of ways
        dp = {}
        def dfs(i, k):
            if i == len(target):
                return 1
            # k reached the end but i havent
            if k == len(words[0]):
                return 0
            if (i, k) in dp:
                return dp[(i, k)]

            c = target[i]
            # skip current k
            dp[(i, k)] = dfs(i, k + 1)
            # use current k
            # multipler account for multiple k position in word in words can satisfy target building at i
            dp[(i, k)] += count[(k, c)] * dfs(i + 1, k + 1)

            return dp[(i, k)] % mod

        return dfs(0, 0)