from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(i):
            if nums[i] == 0:
                nums[i] = 1
            else:
                nums[i] = 0
                
        ans = 0
        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                flip(i)
                flip(i + 1)
                flip(i + 2)
                ans += 1
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return ans