import math
import heapq
from typing import List

class Solution:
    """
    min heap is used to store the distance of each point to the origin
    """
    def calc_dist2orig(self, point):
        return math.sqrt((point[0]-0)**2 + (point[1]-0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(self.calc_dist2orig(pt), pt) for pt in points]
        heapq.heapify(minHeap)
        ans_raw = heapq.nsmallest(k, minHeap)
        ans = [res[1] for res in ans_raw]
        return ans