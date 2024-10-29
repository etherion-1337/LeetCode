from typing import List

class Solution:
    """
    time complexity: O(n) where n is the total number of characters in all strings
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # find the shortest string's len
        shortest_len = min([len(s) for s in strs])
        if shortest_len == 0:
            return ""
        check = True
        for i in range(shortest_len):
            tmp = strs[0][i]
            # check if every string has the same character at the same index
            for s in strs:
                if s[i] == tmp:
                    continue
                else:
                    check = False

            if not check:
                break
            else:
                ans += tmp

        return ans

class NeetSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res