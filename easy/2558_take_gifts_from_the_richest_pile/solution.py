from typing import List
import heapq
import math
from math import sqrt
from math import floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [- gift for gift in gifts]
        heapq.heapify(max_heap)

        while k > 0:
            next_big_gift = heapq.heappop(max_heap)
            _tmp = math.floor(sqrt(-1 * next_big_gift))
            heapq.heappush(max_heap, -1 * _tmp)
            k -= 1
        
        ans = 0
        while max_heap:
            ans = ans + -1 * heapq.heappop(max_heap)

        return ans
    

class NeetSolution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))

        return -sum(gifts)