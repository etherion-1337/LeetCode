from typing import List

class Solution:
    """
    DFS solution
    Each level is branching out to all possible numbers
    if number is already in the current list, skip it, this means choose the next path
    this solution works because the input integers are unique
    """
    def dfs(self):
        # base case
        if len(self.curr) == len(self.nums):
            self.result.append(self.curr.copy())
            return

        for num in self.nums:
            if num in self.curr:
                continue
            self.curr.append(num)
            self.dfs()
            self.curr.pop()

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.curr = []
        self.nums = nums

        self.dfs()

        return self.result