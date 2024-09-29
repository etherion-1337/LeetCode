from typing import List

class Solution:
    """
    Bruteforce solution using DFS with backtracking
    TLE
    """
    def dfs(self, i):
        if i >= len(self.coins) or sum(self.curr) > self.amount:
            return
        elif sum(self.curr) == self.amount:
            self.result.append(len(self.curr.copy()))
            return

        self.curr.append(self.coins[i])
        self.dfs(i)
        self.curr.pop()
        self.dfs(i+1)

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount = amount
        self.curr = []
        self.result = []

        self.dfs(0)
  
        return min(self.result) if self.result else -1
    

class NeetSolution:
    """
    bottom up DP solution

    solve for amount = 0, what is the minimum amount of coin needed -> dp[0]
    then proceed to amount = 1 -> dp[1] then so on ...

    For each amount value, scan through the array of coins, if there is value of amount - curr coin >= 0,
    it means the previous solution of dp[amount - curr coin] can be used, and plus the current coin, this is potentially a new solution at dp[curr amount]

    time complexity: O(amount * len(coins))
    space complexity: O(amount)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp cache for [0,...,amount]
        # this stores the min amount of coin needed for each amount
        # default value is the max value
        dp = [float('inf')]*(amount+1)
        # base case
        dp[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                if value - coin >= 0:
                    dp[value] = min(dp[value], dp[value - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1