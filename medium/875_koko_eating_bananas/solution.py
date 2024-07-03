from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brute force solution
        time complexity: O(max(piles) * n)
        """
        for i in range(max(piles), 0, -1):
            _list = [-(-pile//i) for pile in piles]
            ans = sum(_list)
            if ans > h:
                return i + 1

        return max(piles)
    
class NeetSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        same idea with brute force solution but with binary search
        search from 1 to max(piles) since max(piles) is the upper bound of the answer: eat maximum pile in 1 hour
        time complexity: O(nlog(max(piles))*n)
        """
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            k = (l+r)//2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1

        return ans
    

