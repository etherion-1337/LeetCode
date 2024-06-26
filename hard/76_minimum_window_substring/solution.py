class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Bruteforce solution
        time complexity = O(n^2) where n is the length of s
        """
        if s == t:
            return s

        if len(s) < len(t):
            return ""
        
        if not s:
            return ""

        t_counter = self.get_char_dict(t)
        hash_map = {}

        for l in range(len(s)):
            for r in range(l+1, len(s)+1):
                sub_str = s[l:r]
                sub_counter = self.get_char_dict(sub_str)
                if self.is_contained(t_counter, sub_counter):
                    hash_map[sub_str] = len(sub_str)    
        if not hash_map:
            return ""
        return min(hash_map, key=hash_map.get)

    def is_contained(self, subdict, superdict):
        for k,v in subdict.items():
            if k in superdict:
                if v <= superdict[k]:
                    continue
                else:
                    return False
            else:
                return False
        return True
    
    def get_char_dict(self, s):
        ans = {}
        for char in s:
            if char in ans:
                ans[char] += 1
            else:
                ans[char] = 1
        return ans