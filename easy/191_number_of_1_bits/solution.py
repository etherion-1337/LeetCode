class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = "{0:b}".format(n)
        ans = 0
        for c in bin_str:
            if c == "1":
                ans += 1
        return ans 
    
class NeetSolution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # get last digit
            ans += n%2
            # bit shift to the right by 1
            n = n >> 1

        return ans

class NeetSolution:
    def hammingWeight(self, n: int) -> int:
        """
        this trick need logic AND n with n-1

        if the last bit of a number n is 1, then n-1 will flip the last bit to 0 and the rest remain the same
        if the last bit of a number n is 0, then n-1 will change accordingly e.g. 100000 -> 011111
        """
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res 