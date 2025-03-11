from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_dict = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(s)):
            if s[r] in "abc":
                char_dict[s[r]] += 1
            while len(char_dict) == 3:
                ans += (len(s) - r)
                if s[l] in "abc":
                    char_dict[s[l]] -= 1
                if char_dict[s[l]] < 1:
                    char_dict.pop(s[l])
                l += 1

        return ans