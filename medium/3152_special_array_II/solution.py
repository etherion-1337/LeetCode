from typing import List

class Solution:
    """
    prefix sum solution

    time complexity: O(n + q)
    space complexity: O(n)
    """
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # calculate the longest subarray with alternating parity at each position
        prefix_sum = [1] * len(nums) 
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                prefix_sum[i] = prefix_sum[i - 1] + 1
            else:
                prefix_sum[i] = 1
        # go through the query and check if the subarray length is less than or equal to the longest subarray with alternating parity
        ans = []
        for start, end in queries:
            if end - start + 1 <= prefix_sum[end]:
                ans.append(True)
            else:
                ans.append(False)

        return ans