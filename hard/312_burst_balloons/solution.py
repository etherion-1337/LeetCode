from typing import List

class Solution:
    """
    Bruteforce DFS
    TLE
    """
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(nums):
            if len(nums) == 2:
                return 0

            maxCoins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(nums[:i] + nums[i + 1:])
                maxCoins = max(maxCoins, coins)
            return maxCoins

        return dfs(nums)

class NeetSolution:
    def dfs(self, l, r):
        if l > r:
            return 0
        if (l,r) in self.dp:
            return self.dp[(l,r)]
        
        self.dp[(l,r)] = 0
        for i in range(l, r + 1):
            # coins from curr ballon
            # since it is last to be bursted, its boundary is just outside of L and R
            coins = self.nums[l - 1] * self.nums[i] * self.nums[r + 1]
            # right subarr + left subarr
            coins += self.dfs(l, i - 1) + self.dfs(i + 1, r)
            self.dp[(l,r)] = max(coins, self.dp[(l,r)])
        return self.dp[(l,r)]

    def maxCoins(self, nums: List[int]) -> int:
        """
        2D DP top down

        cache a dict with key (l,r) which is the left and right boundary of sub continuous array.
        we phrase the problem into what is the max coins we can get if we burst the curr ballon LAST.
        this means the curr ballon's left and rigth will be just beyond curr L and R of the subarray -> these will be used to compute curr balloon's coins score
        then we recursivly find the max possible coins from the left and right sub array of the current array
        """
        # we add in the pseudo boundary first, mentioned in the qn
        self.nums = [1] + nums + [1]
        # key: (l,r) which is the left and right boundary of given input
        # value: maximum coins
        self.dp = {}
        # ignore the 2 pseudo boundary
        return self.dfs(1, len(self.nums)-2)

