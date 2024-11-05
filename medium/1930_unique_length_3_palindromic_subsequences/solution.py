import collections

class Solution:
    """
    time complexity: O(26n) ~ O(n)
    space complexity: O(26) ~ O(1)
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set() # (mid char, outside char)
        left = set() # left of the curr char
        right = collections.Counter(s)
        # iterate as the middle char of the paldin
        for mid in range(len(s)):
            right[s[mid]] -= 1 # since its mid, it cannot be in right now
            if right[s[mid]] == 0:
                right.pop(s[mid])

            for j in range(26):
                c = chr(ord("a") + j)
                if c in left and c in right:
                    ans.add((c, s[mid]))
            # now add to the left 
            left.add(s[mid])

        return len(ans)