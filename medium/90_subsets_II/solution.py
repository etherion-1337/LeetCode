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
    

class NeetSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort so that duplicates are adjacent
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # all subsets that exclude nums[i]
            # move pointer to next different number
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset) # even if we run through the while loop, this will gives [] which is still valid

        backtrack(0, [])
        return res