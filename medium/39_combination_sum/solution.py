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
        
class NeetSolution:
    """
    time complexity: O(2^t) where t is the target
    NC's explanation:
    use a binary tree to represent the recursion tree
    one path is to include the first element, the other path is to exclude the first element, which is []
    check his youtube video for more details
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # the path to include the current element
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # the path to exclude the current element, which is []
            # the i + 1 means that it will not include the current element in the other path
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res