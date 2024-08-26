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
    

class NeetSolution:
    """
    Recursive solution
    1. Base case: if nums is empty, return [[]]
    2. Get all permutations of nums[1:]
    3. For each permutation, insert nums[0] at every possible position
    4. Append the new permutation to the result

    Time complexity: O(n! * n^2)
    space complexity: O(n! * n)
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            # since we can insert at len(p) + 1 positions
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
    
        return res
    
class NeetSolution_2:
    """
    Iterative solution
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms