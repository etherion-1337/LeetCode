from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        naive solution
        Time complexity: O(n)
        Space complexity: O(n)
        """
        mod_k = k % len(nums)
        nums_1 = nums[:(len(nums) - mod_k)]
        nums_2 = nums[-mod_k:]
        nums_dup = nums_2 + nums_1
        if k == 0:
            pass
        else:
            for i in range(len(nums)):
                nums[i] = nums_dup[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Neetcode

        similar to the above solution
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(nums)
        tmp = [0] * n
        for i in range(n):
            tmp[(i + k) % n] = nums[i]
        
        nums[:] = tmp


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Neetcode

        using reverse trick
        time complexity: O(n)
        space complexity: O(1)
        This is the most optimal solution.
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)