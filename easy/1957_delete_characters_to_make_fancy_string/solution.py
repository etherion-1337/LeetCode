class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def makeFancyString(self, s: str) -> str:
        tmp = s[0]
        count = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == tmp:
                count += 1
            else:
                tmp = s[i]
                count = 1

            if count < 3:
                ans += s[i]

        return ans