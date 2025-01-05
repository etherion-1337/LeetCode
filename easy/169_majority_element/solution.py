from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        return max(count, key = count.get)