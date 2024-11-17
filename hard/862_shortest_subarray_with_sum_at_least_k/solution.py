from typing import List
from collections import deque
import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        brute force solution

        time complexity: O(n^2)
        space complexity: O(1)
        """
        ans = float("inf")

        for i in range(len(nums)):
            j_ans_found = False
            for j in range(i, len(nums)):
                if j - i + 1 > ans:
                    break
                if sum(nums[i:j+1]) >= k:
                    ans = min(ans, j - i + 1)
                    j_ans_found = True
                if j_ans_found:
                    break
                
        if ans == float("inf"):
            return -1
        else:
            return ans
        
class NeetSolution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        prefix sum solution with min heap

        time complexity: O(nlogn)
        space complexity: O(n)

        not guaranteed to find all sub arr in min heap since we will pop some
        the popped prefix wont be used again with later/larger r since it will only result a bigger size of sub array
        """
        ans = float("inf")

        curr_sum = 0
        min_heap = [] # (prefix_sum, end_idx)

        for r in range(len(nums)):
            curr_sum += nums[r]

            if curr_sum >= k:
                ans = min(ans, r + 1)

            # find the min window ending at r
            while min_heap and curr_sum - min_heap[0][0] >= k:
                prefix, end_idx = heapq.heappop(min_heap)
                ans = min(ans, r - end_idx)
            heapq.heappush(min_heap, (curr_sum, r))

        return -1 if ans == float("inf") else ans
    
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        prefix sum solution with monotonic increasing stack

        time complexity: O(n)
        space complexity: O(n)

        think of it as if monotonic decreasing prefix then it is good to remove the smallest (or last one)
        since it can both maximize the left over sum (i.e. arr - prefix arr) and minmize size of the ans

        therefore we are looking for points of turning (which are monotonic increasing) and put in the deque to try to remove
        """
        ans = float("inf")

        curr_sum = 0
        q = deque() # (prefix_sum, end_idx)

        for r in range(len(nums)):
            curr_sum += nums[r]

            if curr_sum >= k:
                ans = min(ans, r + 1)

            # find the min window ending at r
            while q and curr_sum - q[0][0] >= k:
                prefix, end_idx = q.popleft()
                ans = min(ans, r - end_idx)
            # maintain monotonic increasing stack
            while q and q[-1][0] > curr_sum:
                q.pop()
            q.append((curr_sum, r))

        return -1 if ans == float("inf") else ans

class ClaudeSolution:
    """
    Claude 3.5 sonnet solution
    """
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Create prefix sum array
        # prefix[i] represents sum of elements from index 0 to i-1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Initialize result to n+1 (impossible length)
        min_length = n + 1
        
        # Deque will store indices of prefix sums
        # We maintain it in increasing order of both indices and values
        dq = deque()
        
        # Iterate through all prefix sums
        for right, curr_sum in enumerate(prefix):
            # Remove indices from deque whose values are greater than current sum
            # They can't give us a better answer as any future sum would create
            # a larger subarray with them
            while dq and curr_sum <= prefix[dq[-1]]:
                dq.pop()
                
            # Remove indices from front of deque if they give us valid subarrays
            # Since we want shortest subarray, once an index works, we don't need
            # it anymore for larger right indices
            while dq and curr_sum - prefix[dq[0]] >= k:
                min_length = min(min_length, right - dq[0])
                dq.popleft()
                
            # Add current index to deque
            dq.append(right)
        
        return min_length if min_length <= n else -1