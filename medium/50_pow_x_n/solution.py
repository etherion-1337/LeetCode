class Solution:
    """
    cheese
    """
    def myPow(self, x: float, n: int) -> float:
        return x**n

class Solution:
    """
    time complexity: O(logn)
    """
    def divide_conquer(self, x, n):
        """
        keep divide power by 2
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = self.divide_conquer(x, n//2)
        result = result * result
        # if power is odd, we need another x since the from floor division, we lose one x
        if n%2:
            return result*x
        else:
            return result

    def myPow(self, x: float, n: int) -> float:
        result = self.divide_conquer(x, abs(n))
        if n >= 0:
            return result
        else:
            return 1/result