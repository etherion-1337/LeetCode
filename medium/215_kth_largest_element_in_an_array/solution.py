from typing import List
import heapq

class Solution:
    """
    heap solution
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = nums[0] # dummy
        minHeap = [- num for num in nums]
        heapq.heapify(minHeap)
        while k > 0:
            ans = heapq.heappop(minHeap)
            k -= 1

        return -ans
    
