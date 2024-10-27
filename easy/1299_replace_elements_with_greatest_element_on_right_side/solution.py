from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        # keep track of the largest element from the right
        largest = max(arr[-1], arr[-2])
        ans = [arr[-1], -1]
        # iterate from the third last element to the first element
        for i in range(len(arr)-3, -1, -1):
            largest = max(largest, arr[i+1])
            ans.insert(0, largest)

        return ans
    
class Solution:
    """
    DP solution
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        dp = [-1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            dp[i] = max(arr[i + 1], dp[i + 1])
        return dp
    
class NeetSolution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1

        for i in range(len(arr)-1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr