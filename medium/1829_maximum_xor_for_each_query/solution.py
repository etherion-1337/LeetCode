from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)

    for each answer element, we need to find the maximum number to XOR with a subset of the given array
    note that:
    2^n -> n is the position of the bit and its binary representation is 1 followed by n zeros -> anything less than that will be 1s
    basically we need to make sure there is a 1 correspond to 0 in the maximum XOR results's position, within the boundary of length of the 11111
    """
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # XOR all elements first
        xor = 0
        for n in nums:
            xor ^= n
        # mask is the maximum number that can be XORed with the maximum XOR result (i.e. 11111)
        mask = (1 << maximumBit) - 1
        answer = []

        for n in reversed(nums):
            # use XOR trick to get the bit that we need to flip
            answer.append(xor ^ mask)
            # remove the last element from the XOR result
            xor ^= n

        return answer