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
    
class NeetSolution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        space complexity = O(n) where n is the length of s
        use a sliding window to find the shortest substring that contains all the characters in t
        keep track of the frequency of the characters in t and the frequency of the characters in the window
        also take note how many conditions or unique char with the minimum required frequency met
        """
        count_t = {}
        count_window = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        result_index = [-1, -1]
        result_len = float("infinity")
        # window in s has how many char with the minimum char frequency met in str t
        have = 0 
        # str t's unique char frequency count, determines the number of condition needs to be met
        need = len(count_t)

        l = 0
        for r in range(len(s)):
            count_window[s[r]] = 1 + count_window.get(s[r], 0)

            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                # the preivous r movement makes the substr just met one of the requirement
                have += 1

            # if the condition is met, we want to keep move l pointer to find valid substr
            # that met all conditions
            while have == need:
                # update our shortest result
                if (r - l + 1) < result_len:
                    result_index = [l, r]
                    result_len = r - l + 1
                # pop the left from the window
                count_window[s[l]] -= 1
                # if the left pointer movement made one of the condition not hold
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return s[result_index[0]:result_index[1]+1] if result_len != float("infinity") else ""