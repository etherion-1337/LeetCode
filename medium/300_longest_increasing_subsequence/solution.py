from typing import List

class Solution:
    """
    DP solution
    Time complexity: O(n^2)

    we keep a dp array to store the longest increasing subsequence from i to end
    we iterate from the end of the array to the beginning
    at each index i, we find the max of 1, 1 + dp[i+1], 1 + dp[i+2], ... if nums[i] < nums[i+1]

    the first 1 is actually if the current number by itself is a longest increasing subsequence
    the subquent 1 + x means we can add the current number to the longest increasing subsequence starting from i+1, iff nums[i] < nums[i+1] -> since thats what makes the subsequence increasing
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)