from typing import List

class Solution:
    """
    DFS solution
    very similar to 90. Subsets II
    time complexity: O(n*2^n)
    space complexity: O(n)
    """
    def dfs(self, i):
        if sum(self.curr) == self.target:
            self.result.append(self.curr.copy())
            return
        if i >= len(self.candidates) or sum(self.curr) > self.target:
            return
        # include candidate[i]
        self.curr.append(self.candidates[i])
        self.dfs(i + 1)
        self.curr.pop()
        # skip candidate [i]
        # since the above path will include duplicate as it scan across all elements (including duplicates)
        # this path will skipper duplicates
        # this is to skip duplicates SOLUTION
        # we will still using duplicate numbers if given
        while i + 1 < len(self.candidates) and self.candidates[i] == self.candidates[i+1]:
                i += 1
        self.dfs(i + 1)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.curr = []
        self.target = target
        # sort so that duplicates are adjacent
        self.candidates = sorted(candidates)

        self.dfs(0)
        return self.result
    
class NeetSolution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            # include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res