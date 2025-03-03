from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        pivot_count = 0

        for n in nums:
            if n < pivot:
                small.append(n)
            elif n > pivot:
                large.append(n)
            else:
                pivot_count += 1

        return small + [pivot]*pivot_count + large
    
class NeetSolution:
    """
    2 pointers solution
    """
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, j = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        ans = [0] * len(nums)

        while i < len(nums):
            if nums[i] < pivot:
                ans[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                ans[j2] = nums[j]
                j2 -= 1
            i, j = i + 1, j - 1

        while i2 <= j2:
            ans[i2] = ans[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
        return ans