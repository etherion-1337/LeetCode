from typing import List

class Solution:
    """
    brute force
    """
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str_1, str_2):
            if len(str_1) > len(str_2):
                return False

            if str_2[0:len(str_1)] == str_1 and str_2[-len(str_1):] == str_1:
                return True
            else:
                return False
        ans = 0
        for i in range(0, len(words)):
            for j in range(i, len(words)):
                if i == j:
                    continue
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1

        return ans