import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 - 1
        
        ans = 0
        while x:
            # in python for -ve num, e.g. -1%10 = 9, so we use a math lib
            digit = int(math.fmod(x,10))
            # in python for -ve num, e.g. -1//10 = -1. so we do it this way for int div
            x = int(x/10)
            # we cannot access num > 2147483647 directly due to 32 bit restriction
            # so we compare 214748364 first, if our reversed value is larger than this, then for sure curr_num*10 will be larger
            if (ans > MAX//10 or
               (ans == MAX//10 and digit >= MAX%10)):
               return 0 
            if (ans < MIN//10 or
               (ans == MIN//10 and digit <= MIN%10)):
               return 0
            ans = (ans*10)+digit
        return ans