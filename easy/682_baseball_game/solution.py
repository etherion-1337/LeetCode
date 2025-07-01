from typing import List

class Solution:
    """
    stack solution
    time complexity: O(n)
    space complexity: O(n)
    where n is the number of operations
    """
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for ops in operations:
            if ops == "+":
                ans.append(ans[-1] + ans[-2])
            elif ops == "D":
                ans.append(ans[-1]*2)
            elif ops == "C":
                ans.pop()
            else:
                ans.append(int(ops))

        return sum(ans)
