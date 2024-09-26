class Solution:
    """
    2 pointer solution
    Time complexity: O(n^2)
    
    for each char, expand to left and right to find the longest palindrome string
    """
    def get_palin_str(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > self.result_len:
                self.result = s[l:r+1]
                self.result_len = r - l + 1
            l -= 1
            r += 1

    def longestPalindrome(self, s: str) -> str:
        self.result = ""
        self.result_len = 0

        # odd
        for i in range(len(s)):
            l, r = i, i
            self.get_palin_str(s, l, r)

        # even
        for i in range(len(s)):
            l, r = i, i + 1
            self.get_palin_str(s, l, r)

        return self.result