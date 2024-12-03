from typing import List

class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        str_list = list(s)
        j = 0
        ans = ""

        for i in range(len(str_list)):
            if j < len(spaces) and i == spaces[j]:
                ans += " "
                ans += str_list[i]
                j += 1
            else:
                ans += str_list[i]

        return ans