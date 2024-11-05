class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def minSwaps(self, s: str) -> int:
        open_count, max_open_count = 0, 0

        for c in s:
            if c == "[":
                open_count -= 1
            else:
                open_count += 1
            
            max_open_count = max(max_open_count, open_count)
        # each swap can fix 2 unbalanced brackets
        # +1 is for the case when the number of unbalanced brackets is odd
        return (max_open_count + 1)//2
    

class Solution:
    def minSwaps(self, s: str) -> int:
        opened, closed = 0, 0
        swaps = 0

        for bracket in s:
            if bracket == '[':
                opened += 1
            else:
                closed += 1

            if closed > opened:
                swaps += 1
                opened += 1
                closed -= 1

        return swaps