from collections import defaultdict
from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for k, v in count.items():
            if v % 2:
                return False

        return True
    
class NeetSolution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()

        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)

        return len(odd_set) == 0