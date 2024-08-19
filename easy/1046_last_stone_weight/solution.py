import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.minHeap = [-abs(stone) for stone in stones]
        heapq.heapify(self.minHeap)

        while len(self.minHeap):
            if len(self.minHeap) == 1:
                break

            x = heapq.heappop(self.minHeap)
            y = heapq.heappop(self.minHeap)

            if x == y:
                continue
            else:
                heapq.heappush(self.minHeap, x - y)

        return -self.minHeap[0] if self.minHeap else 0