from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        balls, moves = 0, 0
        for i in range(len(boxes)):
            ans[i] = balls + moves
            moves = moves + balls # this one has to come first
            balls += int(boxes[i])

        balls, moves = 0, 0
        for i in reversed(range(len(boxes))):
            ans[i] += balls + moves # add the value instead
            moves = moves + balls
            balls += int(boxes[i])

        return ans