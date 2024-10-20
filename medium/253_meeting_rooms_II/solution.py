from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        time complexity: O(nlogn)
        space complexity: O(n)

        keep track of the start and end times of the intervals
        when the start time is less than the end time, increment the count -> a meeting has to start
        when the end time is less than the start time, decrement the count -> a meeting has ended
        """
        start = sorted([interval[0] for interval in intervals])
        end = sorted(interval[1] for interval in intervals)
        count = 0
        result = 0
        
        i, j = 0, 0
        # note this condition will exit when either i or j reaches the end of the list
        # for our case i will reach the end of the list first since it is the start time
        # but this means that from this point onwards, there will be no more meetings starting -> count will only decrease
        # so we can safely exit the loop since we have already found the maximum number of meetings that can be held
        while (i < len(start) and j < len(end)):
            if start[i] < end[j]:
                count += 1
                i += 1
            elif end[j] <= start[i]:
                count -= 1
                j += 1
            result = max(result, count)
        return result
    
class NeetSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            time.append((start, 1))
            time.append((end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        count = 0 
        max_count = 0
        for i in time:
            count += i[1]
            max_count = max(max_count, count)
        return max_count