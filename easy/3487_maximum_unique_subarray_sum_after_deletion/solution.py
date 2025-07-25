from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        num_set = set()
        ans = 0
        max_neg = float("-inf")
        neg_count = 0

        for n in nums:
            if n >= 0:
                if n in num_set:
                    continue
                else:
                    ans += n
                    num_set.add(n)
            else:
                max_neg = max(max_neg, n)
                neg_count += 1

        return max_neg if neg_count == len(nums) else ans