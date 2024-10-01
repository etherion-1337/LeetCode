from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        bottom up DP

        we cache a dp where each dp[i] means at s[i] we can find a match word from s[i:]
        """
        # extra space for base case
        dp = [False] * (len(s) + 1)
        # base case where we reach here
        # it is true
        dp[-1] = True

        for i in range(len(s)-1, -1 , -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    # need this step to carry the validity from back to front
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]