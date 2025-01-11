from collections import Counter

class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        char_count = Counter(s)
        odd_char_count = 0
        for c, count in char_count.items():
            if count % 2:
                odd_char_count += 1

        if odd_char_count > k:
            return False
        else:
            return True