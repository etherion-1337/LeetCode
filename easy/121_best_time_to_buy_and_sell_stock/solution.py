class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        brute force solution
        """
        profit = 0

        for i, price in enumerate(prices[:-1]):
            _profit = max(prices[i+1:])-price
            profit = max(_profit, profit)

        return profit
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        time complexity : O(n)
        space complexity : O(1)

        left pointer = buy
        right pointer = sell
        Fix a buy price and find the maximum sell price
        if detected a lower buy price, update the buy price, and the current possible max profit by this buy price is recorded in max_profit
        """
        # left pointer = buy
        # right pointer = sell
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            
            r += 1

        return max_profit