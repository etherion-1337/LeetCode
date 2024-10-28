class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s, idx_t = 0, 0
        while idx_t < len(t) and idx_s < len(s):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
            idx_t += 1
        
        if idx_s == len(s):
            return True
        else:
            return False
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True if i == len(s) else False