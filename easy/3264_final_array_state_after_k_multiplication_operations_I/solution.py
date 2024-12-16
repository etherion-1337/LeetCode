from typing import List
import heapq

class Solution:
    """
    heap solution
    
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = nums.copy()
        min_heap = [(n, i) for i, n in enumerate(nums)]

        heapq.heapify(min_heap)
        while k > 0:
            n, i = heapq.heappop(min_heap)
            ans[i] = n * multiplier
            heapq.heappush(min_heap, (ans[i], i))
            k -= 1
        
        return ans