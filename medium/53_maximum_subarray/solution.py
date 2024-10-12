from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)

        From the 1st element we start addition, as long as the curr sum <0, we reset curr sum -> multiple sub arr
        from these sub arr get the highest one
        """
        # default base
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(curr_sum, max_sum)
        
        return max_sum