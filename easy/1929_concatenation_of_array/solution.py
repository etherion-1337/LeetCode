class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums + nums
        return ans

if __name__ == "__main__":
    soln = Solution()
    _input = [1,2,1]
    answer = soln.getConcatenation(_input)
    print(answer)