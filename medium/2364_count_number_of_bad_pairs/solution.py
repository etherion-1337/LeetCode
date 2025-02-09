from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        total_pairs = 0
        count = defaultdict(int) # unique identifier for int that on the same gradient = 1 line -> num of points on that line

        for i in range(len(nums)):
            total_pairs += i # could use a formula but this is easier
            good_pairs += count[nums[i] - i] # could use gradient but this is easier, add b4 update below, each new point will add pair relation to existing points
            count[nums[i] - i] += 1

        return total_pairs - good_pairs