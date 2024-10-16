from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Greedy algo with min heap

        time complexity: O(nlogn)
        space complexity: O(n)

        keep track of the freq count of each number -> to use to construct number block
        keep track of the smallest element in the heap -> to select the smallest 
        """
        if len(hand) % groupSize:
            return False
        
        # freq count for each num
        count = {}
        for num in hand:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            # the first element in each block of numbers
            first = min_heap[0]
            # for one block of number
            # pop smallest if the freq count is 0
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                # edge case where the element we removed is 0 but it is not the smallest element in the heap
                # this will lead to a hole in the next number block if pop this number
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True