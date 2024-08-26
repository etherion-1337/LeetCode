from typing import List

class Solution:
    """
    DFS solution
    similar to 78. Subsets but we sort the result to remove duplicates
    """
    def dfs(self, i, nums):
        if i >= len(nums):
            if sorted(self.subsets) not in self.result:
                self.result.append(sorted(self.subsets.copy()))
            return
        
        self.subsets.append(nums[i])
        self.dfs(i+1, nums)
        self.subsets.pop()
        self.dfs(i+1, nums)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.subsets = []

        self.dfs(0,nums)
        return self.result