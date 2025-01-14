from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            tmp_a = set(A[:i + 1])
            tmp_b = set(B[:i + 1])

            ans.append(len(tmp_a.intersection(tmp_b)))

        return ans
    
