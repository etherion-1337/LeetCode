import heapq
import copy

class MedianFinder:
    """
    exceed time limit
    """
    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num)

    def findMedian(self) -> float:
        dummy_heap = copy.deepcopy(self.maxHeap)
        if len(dummy_heap)%2 == 0:
            k = len(dummy_heap)//2
            while k > 0:
                ans_1 = heapq.heappop(dummy_heap)
                k -= 1
            ans_2 = heapq.heappop(dummy_heap)
            return (ans_1 + ans_2)/2
        else:
            k = len(dummy_heap)//2
            while k > 0:
                ans_1 = heapq.heappop(dummy_heap)
                k -= 1
            ans_2 = heapq.heappop(dummy_heap)
            return ans_2
        
class NeetMedianFinder:

    def __init__(self):
        # 2 heaps of equal size (max 1 element difference)
        # minHeap store larger portion of value
        # maxHeap store smaller portion of value
        self.small = [] # maxHeap
        self.large = [] # minHeap
        
    def addNum(self, num: int) -> None:
        # incoming num always go to small first
        # -ve since we want maxHeap
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small <= every num in large
        if (self.small and self.large and -1*self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven size correction
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        

    def findMedian(self) -> float:
        # odd number of num in the stream
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # even number of num in the stream
        return (self.large[0] + -1 * self.small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()