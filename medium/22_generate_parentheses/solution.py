from typing import List

class NeetSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Use recursion to generate all possible combinations of parentheses
        time complexity: O(4^n/sqrt(n))
        space complexity: O(n)
        """
        stack = []
        ans = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()

        backtrack(0,0)
        return ans