from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set()

        for i in reversed(range(len(nums))):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                break

        if i == 0 and len(num_set) == len(nums):
            return 0

        return math.ceil((i+1)/3)