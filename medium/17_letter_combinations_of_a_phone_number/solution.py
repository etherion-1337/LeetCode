from typing import List

class Solution:
    """
    time complexity: O(n*4^n)
    """
    def dfs(self, i):
        if len(self.curr) == len(self.digits):
            _temp = self.curr.copy()
            self.result.append("".join(_temp))
            return

        for char in self.digitToChar[self.digits[i]]:
            self.curr.append(char)
            self.dfs(i+1)
            self.curr.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.curr = []
        self.digits = digits

        self.digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits:
            self.dfs(0)

        return self.result
    
class NeetSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res