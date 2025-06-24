from typing import List

class Solution:
    """
    Brute force solution to simulate the problem.
    Time complexity: O(n^2), where n is the length of nums.
    Space complexity: O(n), for storing the indices of key elements.
    """
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_pos = []
        for idx, num in enumerate(nums):
            if num == key:
                key_pos.append(idx)
        
        ans = []
        for idx, num in enumerate(nums):
            for key_idx in key_pos:
                if abs(idx - key_idx) <= k:
                    ans.append(idx)
                    break

        return ans