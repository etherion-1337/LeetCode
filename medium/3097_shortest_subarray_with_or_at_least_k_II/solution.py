from typing import List

class Solution:
    """
    sliding window solution

    time complexity: O(n)
    space complexity: O(1)

    this works because OR operation on the array will only increase the result
    increase R pointer until the OR is greater than k
    then we can move the L pointer to the right until the OR is less than k
    """
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        bits = [0]*32
        # update the bits array
        # given the bits freq array, at each loc of n's binary representation, increase the freq by 1 if it is a 1
        # diff is 1 if we are adding a number, -1 if we are removing a number
        def bits_update(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff
        # convert the bit array into integer
        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        l = 0
        for r in range(len(nums)):
            bits_update(bits, nums[r], 1)
            curr_or = bits_to_int(bits)
            while l <= r and curr_or >= k:
                ans = min(ans, r - l + 1)
                bits_update(bits, nums[l], -1)
                curr_or = bits_to_int(bits)
                l += 1

        return -1 if ans == float("inf") else ans 