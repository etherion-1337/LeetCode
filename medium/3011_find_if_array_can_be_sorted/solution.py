from typing import List

class Solution:
    """
    bubble sort
    time complexity: O(n^2)
    """
    def canSortArray(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] <= nums[j+1]:
                    continue
                else:
                    if bin(nums[j]).count("1") == bin(nums[j+1]).count("1"):
                        # nums[j+1], nums[j] = nums[j], nums[j+1]
                        tmp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = tmp
                    else:
                        return False

        return True
    
class NeetSolution:
    """
    Look for block of numbers with the same set bit
    compare the min and max between blocks
    
    time complexity: O(n)
    space complexity: O(1)
    """
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            return bin(n).count("1")

        # current block's min and max
        # block refer to continuous subarr that has the same set bit
        curr_min, curr_max = nums[0], nums[0]
        prev_max = float("-inf")

        for n in nums:
            # if n is in the current block
            if count_bits(n) == count_bits(curr_min): # always True for last block since there is no next group to jump, need to handle later
                curr_min = min(n, curr_min)
                curr_max = max(n, curr_max)
            else:
                if curr_min < prev_max:
                    return False
                else:
                    prev_max = curr_max
                    # reset to the first num of the block
                    curr_min = n
                    curr_max = n
        # edge case to handle last block
        # because last block will never run the else clause above
        if curr_min < prev_max:
            return False
        
        return True