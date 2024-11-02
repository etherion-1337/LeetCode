from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        bucket sort
        time complexity: O(n)
        space complexity: O(1)

        2 pass solution
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        print(count)
        # pointer on the count arr
        p = 0
        for i in range(0, len(nums)):
            if count[p] != 0:
                nums[i] = p
                count[p] -= 1
            else:
                while count[p] == 0: # if our bucket has [0, 0, X], need skip the first 2 bucket
                    p += 1
                nums[i] = p
                count[p] -= 1

class NeetSolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        time complexity: O(n)
        space complexity: O(1)
        1 pass solution

        inspired by partition step in quicksort
        if 0, move to the front, if 2 move to behind

        edge case due to running i is to the right dir: 
        if i encounter a 2, we could swap a 0 into the middle (and on right of l pointer)
        since i has moved on, the 0 will stay in the middle and caouse problem
        so we do not increase i when we encounter a 2
        the next interation the l pointer will check of 0
        """
        # left and right pointer to the original arr
        # anything left of l is 0, anything right of r is 2
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            else: # nums[i] == 1 case
                i += 1