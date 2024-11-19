from typing import List
from collections import defaultdict

class Solution:
    """
    sliding window (brute force)
    TLE
    """
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr_sum = 0
        l = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            if r - l + 1 > k:
                curr_sum -= nums[l]
                l += 1

            if r - l + 1 == k and len(set(nums[l:r+1])) == k:
                ans = max(ans, curr_sum)

        return ans
    
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        sliding window
        time complexity: O(n)
        space complexity: O(n)
        """
        ans = 0
        curr_sum = 0
        l = 0
        count = {} # count of each number in the window

        for r in range(len(nums)):
            if nums[r] in count:
                count[nums[r]] += 1
            else:
                count[nums[r]] = 1

            curr_sum += nums[r]
            
            if r - l + 1 > k:
                curr_sum -= nums[l]
                count[nums[l]] -= 1
                # remove key if count is 0
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            if r - l + 1 == k and len(count) == k:
                ans = max(ans, curr_sum)

        return ans
    

class NeetSolution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        count = defaultdict(int)
        curr_sum = 0

        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            count[nums[r]] += 1

            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                curr_sum -= nums[l]
                l += 1

            if len(count) == r - l + 1 == k:
                ans = max(ans, curr_sum)

        return ans
    

class NeetSolution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prev_idx = {} # num -> prev index of num
        curr_sum = 0

        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            i = prev_idx.get(nums[r], -1)
            # shift l till the last occur of r
            # because if there is a duplicate the window wont be valid
            # 2nd condition is to check win size
            while l <= i or r - l + 1 > k:
                curr_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                ans = max(ans, curr_sum)

            prev_idx[nums[r]] = r

        return ans