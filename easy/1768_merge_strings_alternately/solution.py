class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ans = []
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                ans.extend(list(word2[j:]))
                break
            if j == len(word2):
                ans.extend(list(word1[i:]))
                break
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1

        return "".join(ans)
    
class NeetSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        ans = []
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
        ans.append(word1[i:])
        ans.append(word2[j:])
        return "".join(ans)