from typing import List

class Solution:
    """
    Brute force solution
    Time complexity: O(n^3)
    Space complexity: O(1)
    """
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = float("-inf")

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = (nums[i] - nums[j]) * nums[k]
                    ans = max(ans, val)

        return ans if ans > 0 else 0
    

class Solution:
    """
    slightly optimized brute force solution
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = float("-inf")
        left = nums[0]
        for j in range(1, len(nums)):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, len(nums)):
                val = (left - nums[j]) * nums[k]
                ans = max(ans, val)

        return ans if ans > 0 else 0