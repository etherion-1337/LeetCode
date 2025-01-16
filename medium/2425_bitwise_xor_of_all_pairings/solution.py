from typing import List

class Solution:
    """
    Brute force solution
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        for n1 in nums1:
            for n2 in nums2:
                ans ^= n1 ^ n2

        return ans
    
class Solution:
    """
    use XOR properties

    time complexity: O(n)
    space complexity: O(1)
    """
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return ans
        elif len(nums1) % 2 and len(nums2) % 2 == 0:
            for n in nums2:
                ans ^= n
        elif len(nums1) % 2 == 0 and len(nums2) % 2:
            for n in nums1:
                ans ^= n
        else:
            for n1 in nums1:
                ans ^= n1
            for n2 in nums2:
                ans ^= n2

        return ans
    
class NeetSolution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        if len(nums2) % 2:
            for n in nums1:
                ans ^= n
        
        if len(nums1) % 2:
            for n in nums2:
                ans ^= n
        
        return ans