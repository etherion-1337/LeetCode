from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
        Hierholzer's algorithm

        1. Create adjacency list and count of edges for each node
        2. Find the starting point (node with count of -1) or any node if not found
        3. Perform DFS to find the euler path
        
        time: O(n)
        space: O(n)
        """
        adj_list = defaultdict(list)
        count = defaultdict(int)

        for src, dst in pairs:
            adj_list[src].append(dst)
            count[src] -= 1
            count[dst] += 1

        start = pairs[0][0] # random if cannot find starting point (i.e. the path is euler circuit)
        for k in adj_list.keys():
            if count[k] == -1:
                start = k
                break
        
        ans = []
        def dfs(curr):
            while adj_list[curr]:
                nxt = adj_list[curr].pop()
                dfs(nxt)
                ans.append([curr, nxt])

        dfs(start)

        return ans[::-1]