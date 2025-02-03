from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        streak = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                streak = max(streak, curr)
                curr = 1
        streak = max(streak, curr)
        
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                curr += 1
                print(curr)
            else:
                streak = max(streak, curr)
                curr = 1
        streak = max(streak, curr)
        return streak
    
class NeetSolution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur = 1
        res = 1
        increasing = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if increasing > 0:
                    cur += 1
                else:
                    cur = 2 # curr plus the prev one
                    increasing = 1
            elif nums[i - 1] > nums[i]:
                if increasing < 0:
                    cur += 1
                else:
                    cur = 2
                    increasing = -1
            else:
                cur = 1
                increasing = 0
            res = max(res, cur)

        return res
         