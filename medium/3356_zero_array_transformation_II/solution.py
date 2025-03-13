from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)

        # if all quries cannot make zero array
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # binary search
        while left <= right:
            mid = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

    def can_form_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        prefix_sum = 0
        diff_arr = [0] * (len(nums) + 1)

        # process first k quries
        for q_idx in range(k):
            start, end, val = queries[q_idx]
            # diff arr can be used reconstruct prefix sum
            diff_arr[start] += val
            diff_arr[end + 1] -= val

        # check if zero arr is possible
        for num_idx in range(len(nums)):
            prefix_sum += diff_arr[num_idx]
            if prefix_sum < nums[num_idx]:
                return False
        return True