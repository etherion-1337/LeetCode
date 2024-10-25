class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            tmp = n%2 # get the last bit
            ans += tmp << (31 - i) # shift left by 31 - i bits
            n = n//2 # shift right by 1 bit, equivalent to n >> 1 if n is positive

        return ans
        

class NeetSolution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # also to get the last bit
            res += (bit << (31 - i))
        return res
    
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i)) # another way is the use OR
        return res