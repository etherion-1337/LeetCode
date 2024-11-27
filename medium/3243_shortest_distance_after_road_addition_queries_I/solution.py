from collections import deque
from typing import List

class Solution:
    """
    BFS solution
    """
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = {i: [i+1] for i in range(n-1)}
        adj_list[n-1] = [] # manually add last node to avoid key not found in BFS
        ans = []
        # BFS
        for src, dst in queries:
            adj_list[src].append(dst)    
            dist = [float("inf")] * n
            q = deque()
            q.append(0)
            dist[0] = 0

            while q:
                curr = q.popleft()
                for adj in adj_list[curr]:
                    if dist[adj] > dist[curr] + 1:
                        dist[adj] = dist[curr] + 1
                        q.append(adj)
            ans.append(dist[-1])

        return ans