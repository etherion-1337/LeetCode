from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        # left pointer = buy
        # right pointer = sell
        l, r = 0, 1
        max_profit = 0
        profit_arr = []

        while r < len(prices):
            if prices[l] < prices[r] and prices[r] > prices[r-1]: # make sure the price is increasing and it is profitable to sell
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                if r == len(prices) - 1: # handle edge case where the last element is the max profit and we need to append it to the profit_arr
                    profit_arr.append(max_profit)
            else: # if we detect a lower buy price, we will sell the stock and update the buy price
                l = r
                profit_arr.append(max_profit)
                max_profit = 0
            r += 1


        return sum(profit_arr)
    
class NeetSolution:
    """
    same idea as above, only look at the increasing price
    but more elegant
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit