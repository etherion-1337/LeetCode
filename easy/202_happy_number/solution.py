class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sum_sq(n)

            if n == 1:
                return True

        return False
        

    def sum_sq(self, num):
        tmp_str = str(num)
        result = 0
        for char in tmp_str:
            result += int(char)**2

        return result
    

class NeetSolution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output

class NeetSolution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sum_of_sq(n)

            if n == 1:
                return True

        return False

    def sum_of_sq(self, n):
        output = 0

        while n:
            digit = n%10
            digit = digit**2
            output += digit
            n = n//10
        return output