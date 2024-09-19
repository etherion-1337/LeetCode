import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra's algorithm
        BFS with minHeap
        time complexity: O(ElogV)

        this is a directed graph problem
        """
        # build adjacency list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # starting condition, weight = 0 for the starting node
        minHeap = [(0,k)]
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            # BFS
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    # need to keep track total time so far
                    # so need w1 + w2
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1