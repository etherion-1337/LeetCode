class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[i] for i in nums]
        return ans

if __name__ == "__main__":
    soln = Solution()
    _input = [0,2,1,5,3,4]
    answer = soln.buildArray(_input)
    print(answer)