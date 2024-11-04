from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        TLE

        time complexity: O(n^2)
        """
        ans_arr = []

        for i in range(0, len(nums)):
            tmp_arr = []
            for j in range(i, len(nums)):
                tmp_arr.append(nums[j])
                if sum(tmp_arr) == k:
                    ans_arr.append(tmp_arr)
                    continue

        return len(ans_arr)
    
class NeetSolution:
    """
    prefix sum solution
    time complexity: O(n)
    space complexity: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        keep track of prefix sum
        as we accumulate sum, we can check prefix combinations that we can drop in order to get k
        we do not reset the hash map after we hit them because they are still valid for subsequet sub arr computation
        """
        # key: prefix sum so far
        # val: freq
        # base case for empty prefix -> arr itself is a subarr so we can remove the empty prefix and still counted
        prefix_sum = {0:1}
        curr_sum = 0
        ans = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            ans += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)

        return ans