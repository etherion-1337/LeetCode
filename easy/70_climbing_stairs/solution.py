class Solution:
    def climbStairs(self, n: int) -> int:
        """
        bottom-up DP

        Time complexity: O(n)
        Space complexity: O(1)

        store a dp array (although we only need two variables to store the previous two steps)
        that represents the number of ways to reach the ith step
        subsequent steps can be calculated by adding the number of ways to reach the previous two steps
        similar to Fibonacci sequence
        """
        one_step, two_step = 1, 1

        for _ in range(n - 1):
            tmp = one_step
            one_step = one_step + two_step
            two_step = tmp

        return one_step