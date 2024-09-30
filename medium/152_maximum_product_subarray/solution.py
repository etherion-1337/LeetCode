from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        DP

        Time complexity: O(n)
        Space complexity: O(1)

        We track the current maximum and minimum product, up to the current element.
        1. note that due to negative value, we can use the current minimum and maximum product multiplied by the current element to get the new maximum and minimum product
        if negative value is encountered, the maximum and minimum product will be swapped
        2. if the current element is 0, we reset the maximum and minimum product to 1 (reset)
        3. note the difference from NeetCode's video is that the max and min is found also with its current value
        -> this is to handle cases such as [-2, -1, -3] where the the min of [-2, -1] will be -1 instead of -2, which avoided a potential 6 (-2*-3) as the max product, since this is forbidden by the question (need contiguous subarray)
        """
        # default value
        result = max(nums)
        curr_max = 1
        curr_min = 1

        for num in nums:
            if num == 0:
                curr_max = 1
                curr_min = 1
                continue
            # tmp placeholder to hold (to update curr_max)
            tmp = curr_max*num
            curr_max = max(curr_min*num, curr_max*num, num)
            # use tmp as curr_max*n has been updated
            curr_min = min(curr_min*num, tmp, num)
            result = max(curr_max, result)
        
        return result