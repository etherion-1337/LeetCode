class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        time complexity = O(nlogn) where n is the length of s2 due to sort
        """
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if sorted(s2[l:r+1]) == sorted(s1):
                return True
            else:
                l += 1
                r += 1
        return False
    
