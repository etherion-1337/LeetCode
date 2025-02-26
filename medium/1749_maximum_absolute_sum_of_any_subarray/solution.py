from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre, max_pre = 0, 0 # max and min prefix sum so far
        cur = 0 # cur prefix sum
        ans = 0

        for n in nums:
            cur += n

            # 2 possbility to achieve either very big or very small sum
            # cur prefix sum - the max or min prefix so far to get both outcomes
            ans = max(ans, abs(cur - min_pre), abs(cur - max_pre))
            min_pre = min(min_pre, cur)
            max_pre = max(max_pre, cur)

        return ans