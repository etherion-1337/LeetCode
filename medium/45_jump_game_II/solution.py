from typing import List

class Solution:
    """
    Greedy solution
    similar to 1D BFS
    
    time complexity: O(n)
    space complexity: O(1)

    maintain a sliding window, when we make a jump, the right boundary of the next window is the furthest we can reach from the current window
    left boundary of the next window is the right boundary of the current window + 1

    we keep track of the number of jumps we made
    """
    def jump(self, nums: List[int]) -> int:
        result = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            furthest = 0
            for idx in range(l, r + 1):
                furthest = max(furthest, nums[idx] + idx)
            l = r + 1
            r = furthest
            result += 1
        return result