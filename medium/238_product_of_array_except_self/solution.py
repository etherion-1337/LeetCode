from typing import List

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        space complexity: O(1)
        time complexity: O(n)

        went through the list twice, once from left to right, and once from right to left
        from left to right: calculate product of all elements to the left of the current element -> prefix
        from right to left: calculate product of all elements to the right of the current element -> postfix, then multiply it with the prefix
        both prefix and post fix store at the same array, so the space complexity is O(1)
        """
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = postfix * ans[i]
            postfix = postfix * nums[i]

        return ans
    
class NeetSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    
