from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visit = set()
        ans = 0

        def dfs(v, res):
            if v in visit:
                return
            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei, res)
            return res

        for v in range(n):
            if v in visit:
                continue
            component = dfs(v, [])
            # if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
            #     ans += 1
            flag = True
            for v2 in component:
                if len(component) - 1 != len(adj[v2]):
                    flag = False
                    break
            if flag:
                ans += 1
        return ans