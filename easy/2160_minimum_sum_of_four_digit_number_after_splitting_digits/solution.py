class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = sorted([int(x) for x in str(num)])
        ans = num_list[0]*10+num_list[2] + num_list[1]*10+num_list[3]
        return ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = 2346
    answer = obj.minimumSum(_input_1)
    print(answer)