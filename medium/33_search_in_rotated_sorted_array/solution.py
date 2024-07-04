from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search solution
        time complexity: O(logn)

        1) first determine if the mid belongs to left or right sorted array
        2) then check if the target is in the left or right side of the mid, by examine the target and the left/right boundary
        3) move the pointer to the correct side
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]: # left sorted array
                if nums[mid] > target:
                    if target < nums[l]: # target is at the right side
                        l = mid + 1
                    else: # target is at the left side
                        r = mid - 1
                else:
                    l = mid + 1
            else: # right sorted array
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if target > nums[r]: # target rotated to left side
                        r = mid - 1
                    else:
                        l = mid + 1 # target remained at right side

        return -1
    
class NeetSolution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1