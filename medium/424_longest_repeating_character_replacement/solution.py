class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        this method loops over all unique characters in the string and uses a sliding window to find the longest substring with the same character.

        n be the number of characters in the string and m be the number of unique characters.

        Time complexity: O(nm). We iterate over each unique character once, which requires O(k) time. We move a sliding window for each unique character from left to right of the string. As the window moves, each character of the string is visited at most two times. Once when it enters the window and again when it leaves the window. This adds O(n) time complexity for each iteration. So the final time complexity is O(nm). For all uppercase English letters, the maximum value of m would be 26.

        Space complexity: O(m). We use an auxiliary set to store all unique characters, so the space complexity required here is O(m). Since there are only uppercase English letters in the string, m=26

        1) find all unique letters in the string
        2) sliding window for each unique letters: 
        2.1) count the number of the letter in the window
        2.2) if the window is valid (r - l + 1) - count <= k, then keep expanding the window and increase count if any of the current letter is added
        2.3) if the window is invalid, then shrink the window from the left side until it is valid and decrease count if any of the current letter is removed
        """
        unique_letters = set(s)
        max_length = 0

        for letter in unique_letters:
            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] == letter:
                    count += 1

                while not (r - l + 1) - count <= k:
                    if s[l] == letter:
                        count -= 1
                    l += 1
            
                max_length = max(max_length, r - l + 1)
        
        return max_length

class NeetSolution1(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Instead of going through all unique char, use a dict to keep track all the char count in the window.
        instead of count above, use max(count.values()) to get the max count of the char in the window.

        time complexity: O(26n) because we need to check the count dict for max value in each iteration.
        """
        count = {}
        ans = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
    
class NeetSolution22:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use maxf to keep track of the max frequency of the char in the window.
        time complexity: O(n)
        """
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)