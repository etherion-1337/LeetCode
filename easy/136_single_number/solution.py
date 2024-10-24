from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        time complexity: O(nlogn) due to sort
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]

        i = 0
        while True:
            # if the last element is the single number
            if i == len(nums) - 1:
                return nums[i]
            else:
                if nums[i] == nums[i+1]:
                    i += 2
                else:
                    return nums[i]
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        
        use XOR
        note that XOR is associative and commutative.
        """
        # default since 0^n = n
        result = 0
        for n in nums:
            result = result^n

        return result