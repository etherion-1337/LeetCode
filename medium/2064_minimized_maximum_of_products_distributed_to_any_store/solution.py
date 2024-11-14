from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        binary search solution

        time complexity: O(Q*log*max(Q))
        """
        def can_distribute(x):
            """
            if x is put in each store, will it exceed the n ?
            if yes it means that we cannot put x in all stores, need bigger val
            in order to distribute all
            """
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n
        # binary search in this range for the optimum x 
        # such that all store can have smallest x
        l, r = 1, max(quantities)
        ans = 0
        while l <= r:
            x = (l + r)//2
            if can_distribute(x):
                ans = x
                r = x - 1
            else:
                l = x + 1

        return ans