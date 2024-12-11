from typing import List

class Solution:
    """
    sliding window

    Time complexity: O(nlogn + n)
    Space complexity: O(1)

    sorting the array to grop the elements that are close to each other
    """
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        nums.sort()

        for r in range(len(nums)):
            # use 2*k because we want to make sure l -> k and k <- r can cover the range
            while nums[r] - nums[l] > 2 * k:
                l += 1

            ans = max(ans, r - l + 1)

        return ans