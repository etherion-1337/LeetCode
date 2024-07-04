from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        cheese solution
        """
        return min(nums)
    
class NeetSolution:
    """
    Binary search solution
    This algo only works for this rotated sorted array
    1) the right sorted array is always greater than the left sorted array
    2) when we exam the mid point, if the mid point is greater than the left point, we know this mid belongs to the left sorted array, we then search the right side.
    3) if the mid point is less than the left point, we know this mid belongs to the right sorted array, we then search the left side to search for a minimum value in the same right sorted array.
    4) if r value is greater than l value, we know this portion is sorted, we can return the l value as the minimum value.
    time complexity: O(logn)
    """
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            mid = (l + r)//2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return ans