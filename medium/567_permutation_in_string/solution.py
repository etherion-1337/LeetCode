import string

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        time complexity = O(n*m) where n is the length of s2 and m is the length of s1
        """
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if sorted(s2[l:r+1]) == sorted(s1):
                return True
            else:
                l += 1
                r += 1
        return False
    
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        using hashmap to store the frequency of each character in s1 and s2
        time complexity = O(26n) where n is the length of s2 and 26 comes from hashmap comparison between s1 and s2
        """
        s1_hash = dict.fromkeys(string.ascii_lowercase, 0)
        s2_hash = dict.fromkeys(string.ascii_lowercase, 0)
    
        for char in s1:
            s1_hash[char] += 1

        l = 0
        r = len(s1) - 1
        for char in s2[:r+1]:
                s2_hash[char] += 1

        while r < len(s2):
            print(s2_hash)
            if s2_hash == s1_hash:
                return True
            l += 1
            s2_hash[s2[l-1]] -= 1
            r += 1
            if r == len(s2):
                break
            s2_hash[s2[r]] += 1
        print(s1_hash)
        return False
    
class NeetSolution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        time complexity = O(26) + O(n) = O(n) where n is the length of s2
        we only need to track matches between s1 and s2's char frequency
        """
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26