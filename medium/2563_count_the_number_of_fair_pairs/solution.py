from typing import List

class Solution:
    """
    brute force solution
    TLE

    time complexity: O(n^2)
    """
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] >= lower and nums[i] + nums[j] <= upper:
                    ans += 1

        return ans
    
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            # return largest i, where nums[i] < target
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            
            return r # l is wrong

        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # the lower and upper bound of the array
            low = lower - nums[i]
            up = upper - nums[i]
            # implemented this way so that we do not need to write 2 bin search
            # the diff is the array size that satisfies the conditions using the ith element
            # i.e. (i, i+1), (i, i+2) , ...,
            ans += (
                bin_search(i + 1, len(nums) - 1, up + 1) - 
                bin_search(i + 1, len(nums) - 1, low)
            )

        return ans