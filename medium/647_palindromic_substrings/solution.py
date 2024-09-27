class Solution:
    """
    solution is similar to the qn 5 longest palindromic substring problem
    """
    def count_palin(self, s, l, r):
        result =  0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        return result

    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            result += self.count_palin(s, l, r)
            # even length palindromes
            l, r = i, i + 1
            result += self.count_palin(s,l, r)

        return result
    
class NeetSolution:
    
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
