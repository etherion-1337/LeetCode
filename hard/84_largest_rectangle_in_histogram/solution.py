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
    
class NeetSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Use stack to keep track of the index of the bars
        if encounter a lower bar, keep poping the stack until the top bar in stack is smaller than the current bar
        at each index we mark the start point
        with each pop, we use the height of the popped bar and the its current index to calculate the area
        key thing is to extend the start index of the newly added bar to the final popped bar in the while loop
        this helps to keep track of the width of the overall rectangle for future bars added into the stack
        time complexity: O(n)
        space complexity: O(n)
        """
        stack = [] # (ind, height)
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                ind, h = stack.pop()
                maxArea = max(maxArea, h*(i - ind))
                start = ind
            stack.append((start, height))

        for i, height in stack:
            maxArea = max(maxArea, height*(len(heights) - i))

        return maxArea