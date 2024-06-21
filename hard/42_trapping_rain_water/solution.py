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