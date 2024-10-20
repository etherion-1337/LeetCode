from typing import List
import heapq

class Solution:
    """
    Brute force solution
    TLE
    time complexity: O(n*m)
    space complexity: O(1)
    """
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []

        for q in queries:
            tmp = float('inf')
            for interval in intervals:
                if interval[0] <= q <= interval[1]:
                    tmp = min(tmp, interval[1]-interval[0]+1)
            if tmp < float("inf"):
                result.append(tmp)
            else:
                result.append(-1)
        return result
    
class NeetSolution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        time complexity: O(nlogn + mlogm)
        space complexity: O(n)

        use min heap to store the length of intervals and end of intervals
        """
        intervals.sort()
        result = {}
        # min heap to store (length, end) of intervals
        min_heap = []
        i = 0

        for q in sorted(queries):
            # add all intervals that start before q -> potentially valid intervals
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            # remove all intervals that end before q -> invalid intervals
            # could be from previous queries or intervals that are not valid since both start and end are before q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # if there is any valid intervals, get the minimum length
            if min_heap:
                result[q] = min_heap[0][0]
            else:
                result[q] = -1

        return [result[q] for q in queries]