from typing import List

class Solution:
    """
    two pointers solution
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r + 1]
