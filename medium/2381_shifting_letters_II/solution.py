from typing import List

class Solution:
    """
    prefix solution

    Time complexity: O(n)
    Space complexity: O(n)
    """
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)

        for start, end, d in shifts:
            if d == 0:
                prefix_diff[end + 1] -= 1
                prefix_diff[start] += 1 # counter the line above so num before start wont be -1
            if d == 1:
                prefix_diff[end + 1] += 1
                prefix_diff[start] -= 1

        diff = 0
        ans = [ord(c) - ord("a") for c in s]

        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            ans[i - 1] = (diff + ans[i - 1]) % 26

        ans_str = [chr(n + ord("a")) for n in ans]

        return "".join(ans_str)