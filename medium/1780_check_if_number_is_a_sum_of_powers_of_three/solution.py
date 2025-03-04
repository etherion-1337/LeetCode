class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        backtrack solution
        """
        
        def backtrack(i, cur):
            if cur == n:
                return True
            if cur > n or 3**i > n:
                return False
            
            # include
            if backtrack(i + 1, cur + 3**i):
                return True
            # dont include
            if backtrack(i + 1, cur):
                return True
        
            return False
            
        return backtrack(0, 0)
    
class NeetSolution:
    """
    maths solution
    """
    def checkPowersOfThree(self, n: int) -> bool:
        # find largest power of 3^i <= n
        i = 0
        while 3**(i+1) <= n:
            i += 1

        # greedy, remove largest powers
        while i >= 0:
            power = 3**i
            if power <= n:
                n -= power

            i -= 1
        
        return n == 0
    
