from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # new interval is before the current interval
            # also the exit condition for the loop if the updated new interval is before the current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # new interval is after the current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # edge case where the updated new interval last all the way to the end of the list
        result.append(newInterval)

        return result