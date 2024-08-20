import math
import heapq
from typing import List

class Solution:
    """
    min heap is used to store the distance of each point to the origin
    heapify is O(n) operation
    popping k element is O(klogn) operation
    if we do sorting it will be O(nlogn) operation
    """
    def calc_dist2orig(self, point):
        return math.sqrt((point[0]-0)**2 + (point[1]-0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(self.calc_dist2orig(pt), pt) for pt in points]
        heapq.heapify(minHeap)
        ans_raw = heapq.nsmallest(k, minHeap)
        ans = [res[1] for res in ans_raw]
        return ans
    
class NeetSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            # if just comparison is needed, we can avoid using sqrt
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res