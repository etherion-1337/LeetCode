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
    
    