class Solution:
    """
    greedy
    time complexity: O(n)
    space complexity: O(1)
    """
    def minChanges(self, s: str) -> int:
        ans = 0 

        for i in range(0, len(s), 2):
            print(i)
            if s[i] != s[i+1]:
                ans += 1

        return ans