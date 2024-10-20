from typing import List

class Solution:
    """
    time complexity: O(nlogn)
    space complexity: O(1)
    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()
        prev_end = intervals[0][1]
    
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
                continue
            else:
                return False
        
        return True
    
class NeetSolution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i:i[0])

        for idx in range(1, len(intervals)):
            i1 = intervals[idx-1]
            i2 = intervals[idx]

            if i1[1] > i2[0]:
                return False

        return True