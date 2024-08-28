from typing import List

class Solution:
    def dfs(self, i):
        # if we searched beyond s, means we found the path that has the right partition
        if i >= len(self.s):
            self.result.append(self.part.copy())
            return
        
        for j in range(i, len(self.s)):
            # proceed dfs iff the current substring is palin
            if self.isPalindrome(self.s, i, j):
                # include the current partition which is palind
                self.part.append(self.s[i:j+1])
                self.dfs(j+1)
                self.part.pop()

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.part = []
        self.result = []

        self.dfs(0)
        return self.result
        