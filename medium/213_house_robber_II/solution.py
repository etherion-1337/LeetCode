from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def rob_linear(self, nums):
        """
        qn 198 solution
        """
        rob_1, rob_2 = 0, 0

        for n in nums:
            tmp = max(rob_2, rob_1 + n)
            rob_1 = rob_2
            rob_2 = tmp

        return rob_2 

    def rob(self, nums: List[int]) -> int:
        """
        run the original algo twice, start from 0 to n-1 and 1 to n
        """
        option_1 = self.rob_linear(nums[1:])
        option_2 = self.rob_linear(nums[:-1])

        # nums[0] is for edge cases that len(nums) == 1
        return max(option_1, option_2, nums[0])