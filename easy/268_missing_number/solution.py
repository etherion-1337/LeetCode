from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums)):
            if n not in nums:
                return n
        
        return len(nums)
    
class NeetSolution:
    def missingNumber(self, nums: List[int]) -> int:
        # we need to initialize the result with the length of the nums because the loop below will not include the last element
        res = len(nums)
        # we basically add all nums in nums and also sum all the nums from 0 to len(nums) where the last element in sum till len(nums) is initialized on top
        # the left over is the missing number
        for i in range(len(nums)):
            res += i - nums[i]
        return res

class NeetSolution:
    """
    XOR solution
    """
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = i ^ nums[i] ^ res
        return res