from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i] # detect cyclic
            safe[i] = False # assume it is not a safe node first
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i] # which is False
            safe[i] = True
            return safe[i] # which is true if abv For loop run all nei

        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans