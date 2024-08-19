import heapq
from typing import List

class Solution:
    """
    heap pop and push are O(logN) operations because of the heap property
    """
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
    
class NeetSolution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        # for edge case where no stone is left after the loop
        stones.append(0)
        return abs(stones[0])