from typing import List

class Solution:
    """
    check from both ends to see where the array is not sorted
    and then from the left array, find the corresponding element from the right

    time complexity: O(n)
    space complexity: O(1)
    """
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # check from left to see where it starts not sorted
        left = 0
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # check from the right 
        right = len(arr) - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # check if the arr is already sorted
        if left >= right:
            return 0

        ans = right # edge case where the front portion need to be removed
        l = 0
        r = right

        # from each sorted left element, find the corresponding num from the right
        # such that if there is a gap we can stitch up
        while l <= left:
            while r < len(arr) and arr[r] < arr[l]:
                r += 1
            ans = min(ans, r - l - 1)
            l += 1

        return ans