from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Brute force solution
        time complexity: O(n^2) for each bar, we check the area with all the bars to the left and right
        """
        ans = 0

        for l, h in enumerate(heights):
            for r in range(l, len(heights)):
                width = r-l+1
                area = width * min(heights[l:r+1])
                ans = max(area, ans)

        return ans