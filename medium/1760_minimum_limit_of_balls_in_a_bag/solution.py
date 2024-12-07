from typing import List
from math import ceil

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(thres):
            """
            given a threshold, determine if all num within nums can be split
            into number smaller (or equal to this threshold)
            within the maxOperations
            """
            ops = 0
            for num in nums:
                # math to determine if a num can be divided in the way we described in docstring
                # this determins the step to divide ball into equal parts
                ops += ceil(num / thres) - 1 
                if ops > maxOperations:
                    return False
            return True

        # binary search
        l, r = 1, max(nums) # search in range of possible ans
        ans = r
        while l < r: # not l <= r to avoid infty as r = m when l also at m
            m = (l + r) // 2
            if can_divide(m):
                # not m - 1, since here we are looking for smallest valid element, not a speifict element
                r = m # m is a valid element, but m - 1 might not
                ans = r
            else:
                l = m + 1

        return ans