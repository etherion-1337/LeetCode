from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        variations of dijkstra algorithm
        we track the max height (or edge) so far and want to find a path has the minimum max path
        instead of find the shortest path

        This problem is asking us to find a path that has the minimize the highest point in the path
        time complexity: O(n^2logn)
        """
        N = len(grid)
        visited = set()
        # (time or max-height, r, c)
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited.add((0,0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            # reached goal
            if r == N - 1 and c == N - 1:
                return t
            # explore 4 dir
            for dr, dc in directions:
                neighR, neighC = r + dr, c + dc
                if (neighR < 0 or neighC < 0 or neighR == N or neighC == N or (neighR, neighC) in visited):
                    continue
                visited.add((neighR, neighC))
                # add in max height so far instead of the current height
                heapq.heappush(minHeap, [max(t, grid[neighR][neighC]), neighR, neighC])