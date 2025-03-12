from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1

        return max(pos, neg)