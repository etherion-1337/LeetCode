from typing import List

class Solution:
    """
    prefix sum

    time complexity: O(n)
    space complexity: O(n)
    """
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_sum = [nums[0]]
        prev = nums[0]

        for i in range(1, len(nums)):
            prev += nums[i]
            prefix_sum.append(prev)

        ans = 0

        for j in range(0, len(nums) - 1):
            if prefix_sum[j] >= total - prefix_sum[j]:
                ans += 1

        return ans
    
class NeetSolution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        ans = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]

            ans += 1 if left >= right else 0

        return ans