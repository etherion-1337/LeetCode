from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        l = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            ans = max(ans, r - l + 1)
            cur = cur ^ nums[r]
        return ans