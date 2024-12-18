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