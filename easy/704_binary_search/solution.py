from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        time complexity: O(logn): log2(n) is the number of times we can divide n by 2
        space complexity: O(1)
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            # this modification is to avoid overflow
            # mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return -1
    
class CheeseSolution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1