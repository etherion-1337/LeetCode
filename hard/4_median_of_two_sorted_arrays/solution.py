from typing import List

class Solution:
    """
    cheesy solution with merge and sort
    time complexity: O((m+n)log(m+n))
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums)%2 == 0:
            mid_1 = int(len(nums)//2)
            mid_2 = int(len(nums)//2) + 1
            return (nums[mid_1-1] + nums[mid_2-1])/2
        else:
            mid = int(len(nums)//2) + 1
            return nums[mid-1]