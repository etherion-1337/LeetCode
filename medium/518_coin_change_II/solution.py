from typing import List

class Solution:
    """
    DFS with backtracking
    TLE

    note the use of point i and i+1 means that when we are i, we cannot go back to i-1, so effectively we are only going forward -> no duplicate. (i.e. 2,2,1 and 2,1,2 are the same)
    """
    def dfs(self, i):
        if i >= len(self.coins) or sum(self.curr) > self.amount:
            return
        elif sum(self.curr) == self.amount:
            self.result.append(self.curr.copy())
            return

        self.curr.append(self.coins[i])
        self.dfs(i)
        self.curr.pop()
        self.dfs(i+1)

    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        self.amount = amount
        self.curr = []
        self.result = []

        self.dfs(0)
  
        return len(self.result)
    

class Solution:
    """
    DFS with memoization

    time complexity: O(n * amount)
    space complexity: O(n * amount)
    """
    def dfs(self, i, curr_amt):
        if curr_amt == self.amount:
            return 1
        if i >= len(self.coins):
            return 0
        if curr_amt > self.amount:
            return 0
        if (i, curr_amt) in self.dp:
            return self.dp[(i, curr_amt)]
        # 2 choices: 
        # 1. take the current coin i and the amount increases by coins[i]
        # 2. skip the current coin i and the amount stays the same
        self.dp[(i, curr_amt)] = self.dfs(i, curr_amt + self.coins[i]) + self.dfs(i + 1, curr_amt)
        return self.dp[(i, curr_amt)]

    def change(self, amount: int, coins: List[int]) -> int:
        self.amount = amount
        self.coins = coins
        self.dp = {}

        result = self.dfs(0,0)
        return result
        
class NeetSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        2D DP bottom up
        cache array of amount + 1 (row) x num of coins + 1 (col)
        at each [r][c] cache the num of combinations using coins at c, c+1,...
        e.g.
        0, 1, 2, 5
        1
        2
        3
        4
        5

        time complexity: O(n * amount)
        space complexity: O(n * amount)
        at each iteraction at [r][c] (for coin type we iterate from the end)
        1) we first check col on the right, thats the option of skipping current coin type and go to the next coin type
        2) we then check curr_amt - current coin value and get the cell at the same col but jump to diff row (which correspond to the num of combination for the remaining amt) and get the cached value there, this is the option of we actually use the current coin type
        we can stay in the same col because we are allowed to reuse the coin type. 

        note the similarity vs the memoization solution: the fact that the dfs is being calculated with the iteration method from the previous iteration round
        note the matrix is transposed when compared to the video
        """
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        # base case
        dp[0] = [1] * (len(coins) + 1)

        for curr_amt in range(1, amount + 1): # r
            for i in range(len(coins) - 1, -1, -1): # c
                dp[curr_amt][i] = dp[curr_amt][i + 1]
                if curr_amt - coins[i] >= 0:
                    dp[curr_amt][i] += dp[curr_amt - coins[i]][i]
        # return [0] since it includes all coin type: from [0] -> the end
        return dp[amount][0]
    
class NeetSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        2D DP bottom up

        time complexity: O(n * amount)
        space complexity: O(n)

        take advantage of we only need to keep track of one row
        note this matrix dimension is the same as the video, hence the row is the coin type and col is the amount
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]