class Solution:
    """
    since we do not have to build the string, we just keep track the length of the string
    """
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]
            
            ans = 1 if length >= low else 0
            ans += dfs(length + zero) + dfs(length + one)

            dp[length] = ans % mod

            return dp[length]

        return dfs(0)