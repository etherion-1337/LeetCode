from typing import List

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        exceed time
        """
        ans = 0

        for i, h in enumerate(height):

            if i == 0 or i == (len(height) - 1):
                continue
        
            l_max = max(height[:i])
            r_max = max(height[i+1:])

            vol = min(l_max, r_max) - h

            if vol < 0:
                continue

            ans = ans + vol

        return ans
    
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        space complexity : O(n)
        memory complexity : O(1)

        track the left_max of left pointer and right_max of right pointer
        at each step, compare the left_max and right_max, and move the pointer with smaller max
        this is because the volume of water is determined by the smaller max
        when calculate min(left_max, right_max) we know that whichever pointer we just moved that max is the smaller one
        """
        ans = 0
        l, r = 0, len(height) - 1

        l_max = height[l]
        r_max = height[r]

        if not height:
            return ans

        while r > l:
            if l_max > r_max:
                r -= 1
                r_max = max(r_max, height[r])
                vol = max(r_max - height[r], 0)
                ans += vol

            else:
                l += 1
                l_max = max(l_max, height[l])
                vol = max(l_max - height[l], 0)
                ans += vol
        
        return ans
    
class NeetSolution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res