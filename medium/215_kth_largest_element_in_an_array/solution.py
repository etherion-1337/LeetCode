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
    
class NeetSolution:
    """
    quick select solution
    average time complexity: O(n), actually 2n
    worst time complexity: O(n^2)

    currently cannot pass the test case.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            # choose right most element as pivot for simplicity
            pivot, p = nums[r], l
            # quick select
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            # look at the left part
            if p > k:
                return quick_select(l, p - 1)
            # look at the right part
            elif p < k:
                return quick_select(p + 1, r)
            # found the kth element
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
    
class NeetSolution2:
    """
    another quick select solution from NeetCode
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill