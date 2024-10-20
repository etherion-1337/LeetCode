from typing import List

class Solution:
    """
    time complexity: O(nlogn)
    space complexity: O(1)
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        result = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                result += 1
                # remove whichever ends later
                # to maximise possiblilty of overlapping in the future
                prev_end = min(prev_end, end)
        return result