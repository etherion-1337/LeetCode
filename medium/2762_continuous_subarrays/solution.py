import collections
from typing import List

class Solution:
    """
    Sliding Window

    Time complexity: O(n)
    Space complexity: O(n)
    """
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        # {key: num, val: freq}
        # keep track of max and min within (l, r), used to move l
        d = collections.defaultdict(int)

        # sliding window to count the num of subarr ending at r (or i in this case)
        for i in range(len(nums)):
            d[nums[i]] += 1
            while max(d.keys()) - min(d.keys()) > 2:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                # move l until window valid again
                # we should have removed all the big num that caused the subarr endding at r to be invalid
                l += 1
            # if 3 element in a subarr, then 3 subarr will end at r
            ans += i - l + 1

        return ans