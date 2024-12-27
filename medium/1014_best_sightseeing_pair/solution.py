from typing import List

class Solution:
    """
    time complexity: O(n)
    """
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        # -1 to account for distance: if 1st element pair with 2nd element, the dist is 1
        cur_max = values[0] - 1
        for i in range(1, len(values)):
            ans = max(ans, values[i] + cur_max)
            # either current max or the current value for the next iter
            # -1 since out pointer moved forward 1 step
            cur_max = max(cur_max - 1, values[i] - 1)

        return ans