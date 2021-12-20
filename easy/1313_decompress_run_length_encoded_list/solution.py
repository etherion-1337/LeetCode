class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_grp = list(zip(nums[0::2], nums[1::2]))
        ans = []
        for i in nums_grp:
            ans += [i[1]]*i[0]
        return ans

if __name__ == "__main__":
    obj = Solution()
    _input_1 = [1,2,3,4]
    answer = obj.decompressRLElist(_input_1)
    print(answer)