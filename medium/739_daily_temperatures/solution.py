from typing import List

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        brute force solution
        time complexity: O(n^2)
        """
        ans = []

        for i, temp in enumerate(temperatures):
            _temp = []
            for j in range(i, len(temperatures)):
                if temperatures[j] > temp:
                    ans.append(j-i)
                    _temp.append(j-i)
                    break
            if not _temp:
                ans.append(0)

        return ans
    

class NeetSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use a monotonic decreasing stack to store the (index, temp) of the temperatures.
        pop the stack until the current temperature is equal or smaller than the top of the stack.
        the index difference of the popped element and the current element is the answer for that index
        time complexity: O(n)
        space complexity: O(n)
        """
        ans = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackT = stack.pop()
                ans[stackInd] = (i - stackInd)
            stack.append((i, temp))

        return ans