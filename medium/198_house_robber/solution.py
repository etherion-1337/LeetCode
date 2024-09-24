from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP

        if we solve this problem in reverse (i.e. breakdown problem and solve from right-most),
        the problem statement is:
        rob = max(nums[0]+rob(nums[2:n]), rob(nums[1:n]))

        if we solve it in order, at every pos (e.g. n), we determine what is the max profit can be 
        achieved from nums[0:n+1] (i.e. includes nth pos)
        at each pos there is 2 choices:
        1. rob the current house + the previous previous house (aggregated) profit since we cannot rob adj house
        2. do not rob current, and take the previous house profit 
        we choose the max one out of the 2
        """
        rob_1, rob_2 = 0, 0 

        # [. . . rob_1, rob_2, n, n + 1, ...]
        for n in nums:
            tmp = max(rob_2, rob_1 + n)
            rob_1 = rob_2
            rob_2 = tmp

        return rob_2