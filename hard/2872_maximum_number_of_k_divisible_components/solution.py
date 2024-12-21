from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        DFS solution

        from bottom up, if a node or subtree has a sum that is divisible by k, then we can add 1 to the answer
        if a returned children can be divided by k, then if we add the current node and also can be divided by k, this means the current node itself can be divided by k and we can add 1 to the answer too
        """
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        ans = 0

        def dfs(curr, parent):
            total = values[curr]

            for child in adj[curr]:
                if child != parent:
                    total += dfs(child, curr)

            if total % k == 0:
                nonlocal ans
                ans += 1
            
            return total
        
        dfs(0, -1)

        return ans