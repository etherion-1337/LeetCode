from typing import List

class Solution:
    """
    greedy solution
    time complexity: O(n)
    space complexity: O(1)
    """
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_max = nums[0]
        max_diff = 0 # max(i - j)
        ans = 0

        for k in range(1, len(nums)):
            ans = max(ans, max_diff * nums[k])
            i_max = max(i_max, nums[k])
            max_diff = max(max_diff, i_max - nums[k])

        return ans