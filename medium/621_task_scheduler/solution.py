from collections import Counter, deque
import heapq
from typing import List

class Solution:
    """
    use heap and queue to keep track of the tasks
    pop and pushing from heap is time complexity: O(n), in this case is O(26)
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # we only keep track of the frequency of each distinct task
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        # keep track next avaiable task and at what time
        # pairs of [-cnt, available at what time step]
        q = deque()

        while q or maxHeap:
            time += 1

            if maxHeap:
                # since values are -ve, we +1 to make it smaller
                # normal logic should be -1
                cnt = 1 + heapq.heappop(maxHeap)
                # if cnt == 0, this task is done
                if cnt:
                    q.append([cnt, time + n])

            # if there is a task available to be processed
            # remove from queue and 
            # push back into the heap (now with lesser frequency)
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time