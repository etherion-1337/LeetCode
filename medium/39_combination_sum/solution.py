from typing import List

class Solution:
    """
    DFS with backtracking
    Very similar to the subset problem Qn 78
    """
    def dfs(self, i):
        # base case
        if i >= len(self.candidates) or sum(self.curr) > self.target:
            return
        elif sum(self.curr) == self.target:
            self.result.append(self.curr.copy())
            return
        # include the current element
        self.curr.append(self.candidates[i])
        # use i here because we can reuse the same element
        self.dfs(i)
        # exclude the current element and move to next element
        self.curr.pop()
        self.dfs(i+1)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.curr = []
        self.target = target
        self.candidates = candidates
        
        self.dfs(0)

        return self.result
        