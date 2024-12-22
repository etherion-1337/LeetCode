from collections import defaultdict
from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        ans = [-1] * len(queries)

        for i, q in enumerate(queries):
            l, r = sorted(q)
            # return ans here because these cases wont work with algo below
            # e.g. if [5, 5, x, x] and query is [0, 1], algo will return 1 but in fact alice cannot go to index = 1
            if l == r or heights[r] > heights[l]:
                ans[i] = r
            else:
                h = max(heights[l], heights[r])
                # r => [(required_height, query_index)]
                groups[r].append((h, i))

        min_heap = []
        # go through all heights and compute at each height position can it answer some queries
        for i, h in enumerate(heights):

            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))

            while min_heap and h > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                ans[q_i] = i

        return ans