from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        dip_count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dip_count += 1
        # check edge case for rotation
        if nums[-1] > nums[0]:
            dip_count += 1

        return True if dip_count <= 1 else False