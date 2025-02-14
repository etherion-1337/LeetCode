class ProductOfNumbers:
    """
    Bruteforce solution
    """

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        ans = 1
        i = len(self.arr) - 1
        while k > 0:
            ans *= self.arr[i]
            i -= 1
            k -= 1
        return ans



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

class ProductOfNumbers:

    def __init__(self):
        self.curr_prod = 1
        self.prod = []

    def add(self, num: int) -> None:
        if num:
            self.curr_prod *= num
            self.prod.append(self.curr_prod)
        else: # if num == 0, we reset the progress
            self.curr_prod = 1
            self.prod = []
        
    def getProduct(self, k: int) -> int:
        if len(self.prod) < k:
            return 0 # there is a 0 within last k elelment
        elif len(self.prod) == k:
            return self.curr_prod
        else:
            return int(self.prod[-1] / self.prod[-1-k])