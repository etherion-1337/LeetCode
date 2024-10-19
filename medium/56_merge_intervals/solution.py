from typing import List

class Solution:
    """
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]

        for start, end in intervals:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        return result