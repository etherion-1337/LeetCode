class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        ans = 0
        end = len(s) - 1
        # remove trailing spaces
        for i in range(len(s)-1, -1, -1):
            print(i)
            if s[i] == " ":
                end -= 1
            else:
                break
        s = s[:end+1]
        # count the last word
        for j in range(len(s)-1, -1, -1):
            if s[j] != " ":
                ans += 1
            else:
                break

        return ans
    
class NeetSolution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        # handle trailing spaces
        while s[i] == " ":
            i -= 1
        # count the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length