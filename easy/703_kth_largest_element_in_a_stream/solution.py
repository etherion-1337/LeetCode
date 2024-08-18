from typing import List
import heapq

class KthLargest:
    """
    heap solution
    time: O(nlogn) for init, O(logn) for add
    """
    def __init__(self, k: int, nums: List[int]):
        # implement minHeap with k size
        # i.e. minHeap with k largest int
        self.minHeap = nums
        self.k = k
        # O(n)
        heapq.heapify(self.minHeap)
        # O(nlogn)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # edge case if the initial list is less tha k
        # only pop if we have more than k element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)