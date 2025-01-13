from collections import Counter

class Solution:
    """
    time complexity: O(n)
    space complexity: O(26)
    """
    def minimumLength(self, s: str) -> int:
        char_count = Counter(s)
        ans = 0
        for c, cnt in char_count.items():
            if cnt % 2:
                ans += 1
            else:
                ans += 2

        return ans