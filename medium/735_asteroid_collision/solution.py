from typing import List

class Solution:
    """
    stack solution
    time complexity: O(n)
    space complexity: O(n)
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [] # stack

        for ast in asteroids:
            while ans and ans[-1] > 0 and ast < 0:
                diff = ans[-1] + ast # look at the sign mainly
                if diff > 0: # left ast win
                    ast = 0 # this trick can break the while loop
                elif diff < 0:
                    ans.pop()
                else:
                    ast = 0
                    ans.pop()

            if ast:
                ans.append(ast)

        return ans
