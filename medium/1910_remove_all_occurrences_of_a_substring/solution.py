class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        pop_length = len(part) - 1 

        for c in s:
            if len(part) == 1: # edge cases
                if c == part:
                    continue
            tmp = stack[-pop_length:]
            tmp.append(c)
            tmp_str = "".join(tmp)
            if tmp_str == part:
                count = pop_length
                while count > 0:
                    stack.pop()
                    count -= 1
            else:
                stack.append(c)

        return "".join(stack)
    

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        M = len(part)

        for c in s:
            stack.append(c)

            if len(stack) >= M:
                if "".join(stack[-M:]) == part:
                    for _ in range(M):
                        stack.pop()

        return "".join(stack)