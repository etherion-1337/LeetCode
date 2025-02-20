from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        num_set = set(nums)
        choices = ['0', '1']
        def backtrack(curr):
            if len(curr) == N:
                candidate = "".join(curr.copy())
                if candidate in num_set:
                    return False
                return candidate
            
            for c in choices:
                curr.append(c)
                res = backtrack(curr)
                if res:
                    return res
                curr.pop()
    
        return backtrack([])