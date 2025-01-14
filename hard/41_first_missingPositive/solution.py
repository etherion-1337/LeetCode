from typing import List

class Solution:
    """
    time complexity: O(nlogn)
    space complexity: O(1)
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 1
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] == ans:
                ans += 1
        return ans
    

class NeetSolution:
    """
    use the array as memory to store the information of the numbers that are in the array
    since the answer exist in [1, ..., len(nums) + 1], these numbers can be map into the input array
    when we iterate through the input array, we mark the corresponding index (which is num[i] - 1) as negative
    this will tell us this number exist in the input array
    
    time complexity: O(n)
    space complexity: O(1)
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1*(len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1