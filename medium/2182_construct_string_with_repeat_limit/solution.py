import heapq
from collections import Counter

class Solution:
    """
    heap solution
    
    time complexity: O(nlog26) = O(n), where n is the length of s
    space complexity: O(26) = O(1)
    """
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq_map = Counter(s)
        max_heap = [(-ord(c), freq) for c, freq in freq_map.items()]
        heapq.heapify(max_heap)
        ans = []

        while max_heap:
            # get the largest char and its freq, then add to ans first
            curr_char, count = heapq.heappop(max_heap)
            curr_count = min(count, repeatLimit)
            ans.append(chr(-curr_char) * curr_count)
            # if there are left over of the largest, it means we need to get the 2nd largest char and use only once
            # max_heap condition for edge case for s = aaaa, and limit =3 , we cannot use all 4
            if count - curr_count > 0 and max_heap:
                next_char, next_count = heapq.heappop(max_heap)
                ans.append(chr(-next_char))
                if next_count > 1:
                    heapq.heappush(max_heap, (next_char, next_count - 1))
                heapq.heappush(max_heap, (curr_char, count - curr_count))

        return "".join(ans)