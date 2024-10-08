class Solution:
    """
    DFS with backtracking
    TLE
    """
    def dfs(self, i):
        if self.curr == self.t:
            self.result.append(self.curr)
            return
        if i >= len(self.s):
            return

        self.curr += self.s[i]
        self.dfs(i + 1)
        self.curr = self.curr[:-1]
        self.dfs(i + 1)

    def numDistinct(self, s: str, t: str) -> int:
        self.s = s
        self.t = t
        self.result = []
        self.curr = ""

        self.dfs(0)

        return len(self.result)
        
class NeetSolution:
    """
    DP with memoization

    time complexity: O(m*n)
    space complexity: O(m*n)
    """
    def dfs(self, i, j):
        if j == len(self.t):
            return 1
        if i >= len(self.s):
            return 0
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        # if the char matches, we can go 2 ways:
        # both s and t increment by 1 OR we continue look for matching char in s and keep t char the same
        # this is to look for duplicate in s that can match t
        if self.s[i] == self.t[j]:
            self.dp[(i,j)] = self.dfs(i + 1, j + 1) + self.dfs(i + 1, j)
        # if don't match, we need to look for next char in s
        # we have to match all char in t so we cannot move the index
        else:
            self.dp[(i,j)] = self.dfs(i + 1, j)
        return self.dp[(i,j)]

    def numDistinct(self, s: str, t: str) -> int:
        """
        DFS with memoization
        """
        self.s = s
        self.t = t
        # key: (i,j) where i,j are the index of s and t
        # val: num of distinct subseq in s[i:] that can match t[j:]
        self.dp = {}

        return self.dfs(0,0)
    
class NeetSolution:
    """
    2D DP
    """
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]
