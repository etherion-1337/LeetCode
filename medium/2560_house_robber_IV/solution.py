from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        l, r = min(nums), max(nums)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans