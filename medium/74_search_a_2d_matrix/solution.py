from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        concat_list = [elem for sublist in matrix for elem in sublist]

        ans = self.binary_search(concat_list, target)

        return ans

    def binary_search(self, arr: List, target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
        return False