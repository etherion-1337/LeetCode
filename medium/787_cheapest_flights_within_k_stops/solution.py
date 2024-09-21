from typing import List

class Solution:
    """
    Bellman-Ford algorithm
    time complexity: O(k * |flights|)

    at each iteration, we update the prices of all nodes based on the prices of the previous iteration
    we will do this k + 1 times, where k is the number of stops allowed
    we will use a temporary array to store the prices of the current iteration such that changes in the current iteration do not affect other steps in current loop
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                # if inf, it means we cannot reach the current source node to start with
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]