class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        brute force
        time complexity: O(n^2)
        """
        if s.isspace():
            return 1

        ans = 0

        for i, char in enumerate(s):
            hash_set = set()
            _ans = 0
            for j in range(i, len(s)):
                if s[j] not in hash_set:
                    hash_set.add(s[j])
                    _ans = max(len(hash_set), _ans)
                else:
                    _ans = max(len(hash_set), _ans)
                    break
            ans = max(ans, _ans)

        return ans
    

class NeetSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)

        Use a sliding window to keep track of the longest substring without repeating characters.
        if duplicate char is found while right pointer is moving, move left pointer to the right until the duplicate char is removed from the window.
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res