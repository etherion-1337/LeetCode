class Solution:
    def dfs(self, i, j):
        """
        i: index for s
        j: index for p
        """
        if i >= len(self.s) and j >= len(self.p):
            return True
        # used up pattern but s still have -> failed
        # the opposite might not be true !
        if j >= len(self.p):
            return False

        match = i < len(self.s) and (self.s[i] == self.p[j] or self.p[j] == ".")
        # handles the "*" case
        if (j+1) < len(self.p) and self.p[j+1] == "*":
            # if one True then overall is True -> only need one path to succeed
            return (self.dfs(i, j+2) or             # don't use *, we skip curr char and the upcoming *
                    (match and self.dfs(i+1, j)))        # can use *, curr char matched, and there is a "*" afterwards, can repeat operation again or terminate with 0
        if match:
            return self.dfs(i+1, j+1)

        return False

    def isMatch(self, s: str, p: str) -> bool:
        """
        DFS brutal

        difficult part is to handle "*"
        if we meet a "*", we go down 2 path:
            1) if the preceding char matches with target, then we can continue to use * -> i+1 but j remain the same -> we matched one in s so can move on, but p[j] can be used
            2) we do not use the * and hence skip to next char in p
        if curr char from both str match or there is a '.' then i+1 and j+1 -> both move on

        sometimes will TLE 
        """
        self.s = s
        self.p = p

        return self.dfs(0,0)
    
class NeetSolution:
    def dfs(self, i, j):
        """
        i: index for s
        j: index for p
        """
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        if i >= len(self.s) and j >= len(self.p):
            return True
        # used up pattern but s still have -> failed
        # the opposite might not be true !
        if j >= len(self.p):
            return False

        match = i < len(self.s) and (self.s[i] == self.p[j] or self.p[j] == ".")
        # handles the "*" case
        if (j+1) < len(self.p) and self.p[j+1] == "*":
            # if one True then overall is True -> only need one path to succeed
            self.cache[(i,j)] = (self.dfs(i, j+2) or             # don't use *, we skip curr char and the upcoming *
                    (match and self.dfs(i+1, j)))        # can use *, curr char matched, and there is a "*" afterwards, can repeat operation again or terminate with 0
            return self.cache[(i,j)]
        if match:
            self.cache[(i,j)] = self.dfs(i+1, j+1)
            return self.cache[(i,j)]
        self.cache[(i,j)] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        """
        DP top down with memoization

        difficult part is to handle "*"
        if we meet a "*", we go down 2 path:
            1) if the preceding char matches with target, then we can continue to use * -> i+1 but j remain the same -> we matched one in s so can move on, but p[j] can be used
            2) we do not use the * and hence skip to next char in p
        if curr char from both str match or there is a '.' then i+1 and j+1 -> both move on 
        """
        self.s = s
        self.p = p
        self.cache = {}

        return self.dfs(0,0)

# BOTTOM-UP Dynamic Programming
class NeetSolution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]