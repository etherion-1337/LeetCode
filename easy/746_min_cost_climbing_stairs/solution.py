from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP
        time complexity: O(n)
        """
        # the goal is to reach +1 of cost array
        # hence add one to indicate the cost is 0
        cost.append(0)

        # from backwards
        # we start the 3nd last value
        # 2nd last value wont change since last value is 0: anything + 0 is the same
        for i in range((len(cost) - 3), -1, -1):
            # get the minimum cost between single jump and double jump
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
        
        # since we can dececide start at 0 or 1
        return min(cost[0], cost[1])