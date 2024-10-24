class Solution:
    """
    cheese solution
    """
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
    

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        # preset a maximum possible answer arr
        ans = [0]*(len(num1) + len(num2))
        # reverse for easier calc
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # answer go to the right index + whatever carry it is from the previous calc
                ans[i1 + i2] += digit # possible it is > 9, will handle later
                # carry to the next
                ans[i1 + i2 + 1] += (ans[i1 + i2] // 10)
                # handle > 9
                ans[i1 + i2] = ans[i1 + i2] % 10
        # handle leading zero after reversing ans
        ans, beg = ans[::-1], 0
        while beg < len(ans) and ans[beg] == 0:
            beg += 1
        # change back to str
        ans = map(str, ans[beg:])
        return "".join(ans)