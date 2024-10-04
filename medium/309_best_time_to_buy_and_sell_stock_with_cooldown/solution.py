from typing import List

class Solution:
    """
    DP solution with cache

    each cell in the dp table represents the max profit we can get from day i to the end of the prices array

    at each point, we have 2 choices: buy (or cd) or sell (or cd), except for the 1st day, we can only buy (or cd) -> which means on the second day we can only sell (or cd).

    time complexity: O(n)
    """
    def dfs(self, i, l2buy):
        # base case
        if i >= len(self.prices):
            return 0
        # hit a cache
        if (i, l2buy) in self.dp:
            return self.dp[(i, l2buy)]
        # if we looking to buy on day i, we have 2 choices: buy or cd
        if l2buy:
            # the next day we cannot buy
            # since we bought, we need to minus our the price on day i from our potential profit
            buy = self.dfs(i+1, not l2buy) - self.prices[i]
            # cd means we dont do anything and we can still buy on the 2nd day
            cd = self.dfs(i+1, l2buy)
            # we get the best profit from these 2 possible actions
            self.dp[(i, l2buy)] = max(buy, cd)
        else:
            # if we sell, we are forced to cd, i.e. skip a day, and we can buy again on the i+2 day
            # since we sold, we add the price to our profit
            sell = self.dfs(i+2, not l2buy) + self.prices[i]
            cd = self.dfs(i+1, l2buy)
            self.dp[(i, l2buy)] = max(sell, cd)

        return self.dp[(i, l2buy)]
    def maxProfit(self, prices: List[int]) -> int:
        # cache -> key: (i, l2buy), val: max profit
        # l2buy = "looking to buy"
        self.dp = {}
        self.prices = prices

        best_profit = self.dfs(0, True)
        return best_profit
        