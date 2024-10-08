class Solution:
    def dfs(self, i, j):
        # have to be both out of bound -> there could be 1 str out of bound but other str can still provide char
        if i >= len(self.s1) and j >= len(self.s2):
            return True
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        # if s1[i] is used, go to next char in s1 since we cannot reuse
        if i < len(self.s1) and self.s1[i] == self.s3[i+j] and self.dfs(i + 1, j):
            return True
        if j < len(self.s2) and self.s2[j] == self.s3[i+j] and self.dfs(i, j+1):
            return True
        # just cache the False, since once we found 1 True we return all the way up and done
        self.dp[(i,j)] = False
        return False
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        DFS with memoization

        time complexity: O(n*m) where n = len(s1) and m = len(s2), since there are n*m states in cache
        space complexity: O(n*m) for cache
        """
        # key: (i,j) -> index at s1 and s2, index in s3 = i + j
        # val: bool -> if s1[i] or s[j] matches s3[i+j]
        self.dp = {}
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

        if len(self.s1) + len(self.s2) != len(self.s3):
            return False
        return self.dfs(0,0)
    
class NeetSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        2D bottom up DP

        cache a 2D grid with len(s1)+1 * len(s2)+1
        the extra row and col is to handle cases where one str run out but the other str can still provide char
        each cell dp[i][j] is a bool for if char in s1[i:] + s[j:] can form s3[i+j:]
        
        at each cell we can look right and down to check T/F, if either is T we can fill T -> since we can go both way (i..e choose diff str to match)
        """
        if len(s1) + len(s2) != len(s3):
            return False
        # extra row and col
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # base case, if both out of bound, then it is True
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # same as memoization
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]