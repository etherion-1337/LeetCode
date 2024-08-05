from typing import List

class Solution:
    """
    Floyd's Tortoise and Hare (Cycle Detection)
    rephrase the problem to a linked list problem: the value of the array is the index of the next element
    time: O(n)
    space: O(1)
    Refer to NeetCode's solution: https://www.youtube.com/watch?v=wjYnzkAhcNk

    1. Find the intersection point of the slow and fast, these two pointers will meet if cycle is detected
    2. Find the entrance of the cycle:
    the distance of the overlap of fast and slow pointers to the entrance of the cycle is equal to the distance of the head to the entrance of the cycle
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # first phase: find the intersection point of the slow and fast pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # second phase: find the entrance of the cycle
        # if the distance from head to the entrance is very long, then slow pointer will loop many rounds in cycle
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow