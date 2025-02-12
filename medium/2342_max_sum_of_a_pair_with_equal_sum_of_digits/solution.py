from typing import List
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            total = 0
            for d in str(num):
                total += int(d)
            return total

        dsum_num = {} # digit sum -> number

        for n in nums:
            dsum = sum_digits(n)
            if dsum not in dsum_num:
                dsum_num[dsum] = [-n]
                heapq.heapify(dsum_num[dsum])
            else:
                heapq.heappush(dsum_num[dsum], -n)

        ans = -1
        for k, v in dsum_num.items():
            if len(v) >= 2:
                v1 = -heapq.heappop(v)
                v2 = -heapq.heappop(v)
                ans = max(ans, v1 + v2)

        return ans