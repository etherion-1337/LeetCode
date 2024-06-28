class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        time complexity: O(n)
        space complexity: O(n)
        brute force solution
        check each character in the string can close the bracket (if it is a close bracket)
        """
        bracket_open = ["(","{", "["]
        bracket_close = [")", "}", "]"]

        bracket_list = []

        for char in s:
            if char in bracket_open:
                bracket_list.append(char)
            if char in bracket_close:
                if not bracket_list:
                    return False
                converted_char = self.convert_bracket(char)
                if bracket_list[-1] == converted_char:
                    bracket_list.pop()
                else:
                    return False
        if bracket_list:
            return False
        else:
            return True

    def convert_bracket(self, c):
        convert_dict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        return convert_dict[c]
    

class NeetSolution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        time complexity: O(n)
        space complexity: O(n)
        stack is implemented as list in python in this question
        """
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack