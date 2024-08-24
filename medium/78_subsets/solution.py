from typing import List

class Solution:
    """
    Backtracking with DFS
    at each step, we have 2 choices: include the current element or not
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                result.append(subsets.copy())
                return
            
            # include the current element
            subsets.append(nums[i])
            dfs(i+1)
            # exclude the current element
            subsets.pop()
            dfs(i+1)
        
        dfs(0)
        return result