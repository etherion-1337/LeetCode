class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = [i for i in s]
        s_list.sort()
        t_list = [i for i in t]
        t_list.sort()

        return True if s_list == t_list else False
    
class NeetSolution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        lower space complexity since sometimes we assume sorting do not take up space.
        """
        return sorted(s) == sorted(t)
        
class NeetSolution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        space complexity: O(n) or O(s+t) -> stores hash table for s and t
        time complexity: O(n) or O(s+t) -> iterate through s and t
        """
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1

        if s_hash == t_hash:
            return True
        else:
            return False