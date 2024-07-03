from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brute force solution
        """
        for i in range(max(piles), 0, -1):
            _list = [-(-pile//i) for pile in piles]
            ans = sum(_list)
            if ans > h:
                return i + 1

        return max(piles)
    

