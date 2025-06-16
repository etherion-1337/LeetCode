from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        brute force solution
        Time complexity: O(n^2)
        """
        max_diff = -1

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    max_diff = max(max_diff, nums[j] - nums[i])

        return max_diff