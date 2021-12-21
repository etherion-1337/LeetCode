class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_ans, prod_ans = 0, 1
        while n:
            q, r = divmod(n, 10)
            sum_ans += r
            prod_ans *= r
            n = q
        return prod_ans-sum_ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = 234
    answer = obj.subtractProductAndSum(_input_1)
    print(answer)