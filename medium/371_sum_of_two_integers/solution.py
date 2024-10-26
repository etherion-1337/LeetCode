class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        bit manipulation

        in python, the integer is is larger than 32 bits, so we need to mask the result with 0xffffffff (which is just 32 1's)
        ANDing a number with the mask 0xffffffff, or 32 1's, basically turns all of a number's bits into 0's except for the rightmost 32. As a result, the number can be represented as if it only has 32 bits.
        """
        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        # python's negative number is represented by unlimited leading 1's in front
        # if negative number, we need to convert it to a format that python can understand
        # (...000)11111111111111111111111111111101 -> (...111)11111111111111111111111111111101
        # leading 0 is due to the mask
        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a