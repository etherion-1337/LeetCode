from typing import List
import heapq

class Solution:
    """
    Prim's algorithm
    BFS with min heap
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # building adjacency list
        N = len(points)
        # i: list of [cost, node]
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                # since it is undirected, add in both
                adj[i].append([cost, j])
                adj[j].append([cost, i])

        # prim's algo
        result = 0
        visited = set()
        minHeap = [[0,0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            result += cost
            visited.add(i)
            for neighbor_cost, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [neighbor_cost, neighbor])
        return result