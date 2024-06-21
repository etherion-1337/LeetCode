class Solution(object):
    """
    Bruteforce solution
    O(n^2) time complexity
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0

        for i, height_i in enumerate(height):
            for j, height_j in enumerate(height):

                if i == j:
                    continue

                width = j - i
                area = min(height_i, height_j) * (width)

                if area > ans:
                    ans = area

        return ans
    

class Solution(object):
    """
    Use left and right pointers to find the maximum area.
    Since the area is limited by the shorter height, we move the pointer to the shorter height after each iteration.
    O(n) time complexity
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1

        ans = 0

        while l != r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return ans
    
class NeetSolution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res