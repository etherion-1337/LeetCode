class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(n):
            ans = 0
            while n > 0:
                ans += 1 & n
                n = n >> 1
            return ans

        count_1, count_2 = count_bits(num1), count_bits(num2)
        x = num1
        i = 0

        # remove least significant
        while count_1 > count_2:
            if x & (1 << i):
                count_1 -= 1
                x = x ^ (1 << i)
            i += 1

        
        # add least significant
        while count_1 < count_2:
            if x & (1 << i) == 0:
                count_1 += 1
                x = x | (1 << i)
            i += 1

        return x