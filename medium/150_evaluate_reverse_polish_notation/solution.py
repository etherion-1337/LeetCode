from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use stack to store the numbers and pop the top 2 numbers to calculate the result
        insert the result back to the top of the stack
        time complexity: O(n)
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
    
class NeetSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
    
