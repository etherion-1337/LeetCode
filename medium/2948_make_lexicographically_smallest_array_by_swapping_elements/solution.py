from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        first group the numbers to make sure the difference between adjacent numbers in the same group is less than or equal to limit
        these groups can be sorted independently, in their original position
        """
        groups = [] # group of queues
        num_to_grp = {} # nums[i] -> grp

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_grp[n] = len(groups) - 1

        ans = []
        for n in nums:
            j = num_to_grp[n]
            ans.append(groups[j].popleft())

        return ans