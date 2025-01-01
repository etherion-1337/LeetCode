class Solution:
    """
    brute force
    """
    def maxScore(self, s: str) -> int:
        ans = 0

        for i in range(1, len(s)):
            _ans = s[:i].count("0") + s[i:].count("1")
            ans = max(ans, _ans)

        return ans
    
class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            ans = max(ans, one + zero)

        return ans