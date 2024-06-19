class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = s.split()
        concat_str = "".join(s_list)
        alpha_num_str = ""
        for char in concat_str:
            if char.isalnum():
                alpha_num_str += char.lower()

        i = 0
        j = len(alpha_num_str)-1

        while j > i:
            if alpha_num_str[i] != alpha_num_str[j]:
                print(i)
                print(j)
                return False
            i += 1
            j -= 1

        return True
    
class NeetSolution:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

class NeetSolution:
    def isPalindrome(self, s: str) -> bool:
        """
        semi cheating with inbuild functions
        """
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]