from typing import List

class Solution:
    """
    brute force solution

    time complexity: O(n^2)
    space complexity: O(n)
    """
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for w_1 in words:
            for w_2 in words:
                if w_1 in w_2 and w_1 != w_2:
                    ans.add(w_1)
                    break

        return list(ans)