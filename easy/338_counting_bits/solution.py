from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for tmp_n in range(n+1):
            ans.append("{0:b}".format(tmp_n).count("1"))
        
        return ans
    
class Solution:
    """
    brute force 
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            tmp = 0
            while num > 0:
                if num % 2 == 1:  # Check if the last bit is 1
                    tmp += 1
                num = num // 2  # Shift right by 1 bit (integer division)
            ans.append(tmp)
        
        return ans
    
class NeetSolution:
    """
    dp solution
    """
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        # offset is the power of 2
        # find the leading 1 in the binary representation -> determines where to look for in the dp array
        # everytime we reach a power of 2, the leading 1 will be moved to the left by 1
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp