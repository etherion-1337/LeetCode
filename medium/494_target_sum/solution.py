from typing import List

class Solution:
    """
    DFS with backtracking
    time complexity: O(2^n)
    TLE
    """
    def eval(self, curr):
        val = 0
        for i, sign in curr:
            if sign == "+":
                val += self.nums[i]
            else:
                val -= self.nums[i]
        return val

    def dfs(self, i):
        if i > len(self.nums):
            return
        if self.eval(self.curr) > self.target and i == len(self.nums):
            return
        if self.eval(self.curr) == self.target and i == len(self.nums):
            self.result.append(self.curr.copy())
            return
        
        self.curr.append((i, "+"))
        self.dfs(i + 1)
        self.curr.pop()
        self.curr.append((i, "-"))
        self.dfs(i + 1)
        self.curr.pop()

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.curr = []
        self.result = []
        self.dfs(0)

        return len(self.result)
    
class NeetSolution:
    """
    DFS with backtracking with caching/memoization

    time complexity: O(n*sum(nums))
    """
    def dfs(self, i, curr_sum):
        if i >= len(self.nums):
            return 1 if curr_sum == self.target else 0
        if (i, curr_sum) in self.dp:
            return self.dp[(i, curr_sum)]

        # 2 options, either + or - for the curr element, then move to the next
        plus_option = self.dfs(i + 1, curr_sum + self.nums[i])
        minus_option = self.dfs(i + 1, curr_sum - self.nums[i])
        self.dp[(i, curr_sum)] = plus_option + minus_option
        return self.dp[(i, curr_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # key: (index in nums, curr_sum from [0:index+1] with variations of signs)
        # val: # of ways to reach target given at the current index and beyond, and the current sum
        self.dp = {}
        self.nums = nums
        self.target = target

        return self.dfs(0,0)