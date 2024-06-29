from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use stack to store the numbers and pop the top 2 numbers to calculate the result
        insert the result back to the top of the stack
        """
        stack = []
        sign = ["+", "-", "/", "*"]

        for tok in tokens:
            if tok not in sign:
                stack.append(tok)
            else:
                if tok == "+":
                    _top = int(stack[-2]) + int(stack[-1])
                elif tok == "-":
                    _top = int(stack[-2]) - int(stack[-1])
                elif tok == "*":
                    _top = int(stack[-2]) * int(stack[-1])
                elif tok == "/":
                    _top = int(int(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(_top)
        return int(stack[0])
    
