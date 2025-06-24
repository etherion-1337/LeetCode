from typing import List

class Solution:
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