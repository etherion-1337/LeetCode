from typing import List

class Solution:
    """
    Bruteforce solution
    Time complexity: O(n^2)
    space complexity: O(1)
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                if i == j:
                    continue
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break

        return prices
    
class Solution:
    """
    monotonic stack solution
    """
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [p for p in prices]
        # indexes, values are increasing order
        stack = [] # monotonic increasing stack

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res