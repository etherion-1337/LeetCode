from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, curr = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                ans = max(ans, curr)
                curr = nums[i]

        ans = max(ans, curr)
        return ans