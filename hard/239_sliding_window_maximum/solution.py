import collections
from typing import List

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        brute force solution
        time complexity = O(n*k) where n is the length of nums
        """
        l = 0
        r = k - 1

        ans = []

        while r < len(nums):
            _list = nums[l:r+1]
            ans.append(max(_list))
            l += 1
            r += 1
        
        return ans
        
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        using deque as a monotonic decreasing queue
        using deque to store
        time complexity = O(n) where n is the length of nums

        for every new element added to the window, we remove all elements that are smaller than the new element, thus queue[0] is always the maximum element in the window
        if the left pointer is at the maximum element, we remove it from the queue as the window will slide over in the next step
        """
        out = []
        r,l = 0,0
        q = collections.deque()
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            if r+1 >= k:
                out.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l+=1
            r+=1
        return out
    
class NeetSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Same as the above solution but store index instead of value in the deque
        """
        output = []
        q = collections.deque()  # index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove left value from q if the window slides over it
            if l > q[0]:
                q.popleft()
            # this if is an edge case handling because we start r from 0
            # need to make sure the window is of size k before we start adding to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output