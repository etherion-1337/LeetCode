from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        return max(count, key = count.get)
    
class NeetSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        ans, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            ans = n if count[n] > maxCount else ans
            maxCount = max(count[n], maxCount)
        return ans
    
class NeetSolution:
    """
    Boyer-Moore majority vote algorithm

    Time complexity: O(n)
    space complexity: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        ans, count = 0, 0

        for n in nums:
            if count == 0:
                ans = n
            count += (1 if n == ans else -1)
        return ans