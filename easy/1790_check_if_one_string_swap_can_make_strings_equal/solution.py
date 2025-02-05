class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        if not diff:
            return True

        if len(diff) > 2:
            return False

        if len(diff) == 2:
            i, j = diff[0], diff[1]
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False

        return len(diff) == 2
    

class NeetSolution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
            if len(diff) > 2:
                return False

        if len(diff) == 2:
            i, j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]

        return len(diff) == 0