from typing import List

class Solution:
    """
    Sliding Window Technique
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        l = 0
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                ans = min(ans, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return 0 if ans == float("inf") else ans