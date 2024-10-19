class Solution:
    """
    greedy solution
    time complexity: O(n)
    space complexity: O(1)

    we keep track of the number of minimum and maximum possible left parentheses
    """
    def checkValidString(self, s: str) -> bool:
        left_max, left_min = 0, 0

        for char in s:
            if char == "(":
                left_max += 1
                left_min += 1
            elif char == ")":
                left_max -= 1
                left_min -= 1
            else:
                left_min -= 1
                left_max += 1
            # if left_max < 0, then it is impossible to balance the string since we do not have enough left parentheses
            # only ) will decrease left_max -> ))( will not be balanced
            if left_max < 0:  
                return False
            # reset left_min to 0 because we need valid string
            if left_min < 0:
                left_min = 0
        
        return True if left_min == 0 else False
    
class Solution:
    """
    DP with memoization
    time complexity: O(n^3)
    space complexity: O(n^2)
    """
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (
                    dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
                )
            return dp[(i, left)]

        return dfs(0, 0)