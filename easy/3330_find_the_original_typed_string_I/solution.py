class Solution:
    """
    time complexity: O(n)
    space complexity: O(1)
    This solution counts the number of possible strings by checking consecutive characters.
    """
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                ans += 1

        return ans