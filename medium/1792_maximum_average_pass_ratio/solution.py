from typing import List
import heapq

class Solution:
    """
    Heap solution

    time complexity: O(nlogn), where n is the number of classes
    space complexity: O(n)
    """
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        # we track the increase in passing ratio in each class IF a student is added
        for c in classes:
            increase_rate = (c[0] + 1)/(c[1] + 1) - (c[0])/(c[1])
            max_heap.append((-1 * increase_rate, c[0], c[1]))

        heapq.heapify(max_heap) 
        
        # we choose the class with the highest increase in passing ratio IF we added a student
        while extraStudents > 0:
            _, pass_i, total_i = heapq.heappop(max_heap)
            new_increase_rate = (pass_i + 2)/(total_i + 2) - (pass_i + 1)/(total_i + 1)
            heapq.heappush(max_heap, (-1 * new_increase_rate, pass_i + 1, total_i + 1))
            extraStudents -= 1
        
        # calculate the average passing ratio
        counter = 0
        total = 0
        while max_heap:
            _, pass_i, total_i = heapq.heappop(max_heap)
            total += pass_i / total_i
            counter += 1

        return total/counter