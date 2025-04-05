from typing import List

class Solution:
    """
    time: O(2^n)
    space: O(n)
    """
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            if i == len(nums):
                return total

            choose = dfs(i + 1, total ^ nums[i])
            skip = dfs(i + 1, total)

            return choose + skip

        return dfs(0, 0)