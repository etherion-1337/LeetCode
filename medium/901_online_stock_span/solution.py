class StockSpanner:
    """
    stack-based solution
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        for p in reversed(self.stack):
            if p <= price:
                ans += 1
            else:
                break
        self.stack.append(price)
        return ans
        
class StockSpanner:
    """
    monotonic stack solution
    Time Complexity: O(n) 
    Space Complexity: O(n) 
    """
    def __init__(self):
        self.stack = [] # (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)