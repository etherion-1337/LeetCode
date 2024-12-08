from typing import List
import heapq

class Solution:
    """
    greedy solution with min heap

    Time complexity: O(nlogn)
    Space complexity: O(n)

    note that only (maximum) two events can be selected
    """
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        min_heap = []

        best_prev = float("-inf")
        best = max(v for _, _, v in events)

        for start, end, val in events:
            # current sweepline is at "start"
            # process all previous "end" from before "start"
            # find the best value from previous events
            while min_heap and min_heap[0][0] < start:
                _, new_val = heapq.heappop(min_heap)
                best_prev = max(best_prev, new_val)

            heapq.heappush(min_heap, (end, val))
            best = max(best, best_prev + val)

        return best