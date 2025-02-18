class NeetSolution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i in range(len(pattern) + 1):
            stack.append(i + 1) # for D cases, it increasing in stack and later decreasing when popping

            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
            
        return "".join(res)