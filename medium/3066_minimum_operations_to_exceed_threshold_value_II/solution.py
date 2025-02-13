from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = nums.copy()
        heapq.heapify(min_heap)
        ans = 0

        while len(min_heap) >= 2:
            v1 = heapq.heappop(min_heap)
            v2 = heapq.heappop(min_heap)
            if v1 >= k:
                return ans
            elif v2 >= k:
                return ans + 1
            else:
                tmp = min(v1, v2)*2 + max(v1, v2)
                heapq.heappush(min_heap, tmp)
                ans += 1
        return ans