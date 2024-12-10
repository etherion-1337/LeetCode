import string

class Solution:
    """
    Brute force solution

    time: O(26 * n^3)
    space: O(1)
    """
    def maximumLength(self, s: str) -> int:
        best = -1

        for c in string.ascii_lowercase:
            curr_len = max(best + 1, 1) # since best default is -1, need +1
            changed = True
            while changed:
                changed = False
                count = 0
                curr_prefix = c * curr_len
                # scan s for current prefix
                for i in range(len(s)):
                    if s[i:].startswith(curr_prefix):
                        count += 1
                # increase prefix lengh
                if count >= 3:
                    changed = True
                    best = max(best, curr_len)
                    curr_len += 1
                else:
                    break

        return best