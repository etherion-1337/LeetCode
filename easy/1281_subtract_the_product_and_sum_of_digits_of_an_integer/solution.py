class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_list = [int(i) for i in list(str(n))]
        sum_ans = sum(digit_list)
        prod_ans = 1
        for i in digit_list:
            prod_ans = prod_ans*i
        return prod_ans - sum_ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = 234
    answer = obj.subtractProductAndSum(_input_1)
    print(answer)