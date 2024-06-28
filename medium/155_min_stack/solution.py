class MinStack(object):
    """
    This class's getMin() method is O(n) time complexity which is not optimal.
    """

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):
    """
    This class's getMin() method is O(1) time complexity.
    Use 2 stacks, one for the actual stack and the other for the minimum values.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        
    def pop(self) -> None:
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self) -> int:
        """
        :rtype: int
        """
        return self.min_stack[-1]

class NeetMinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]