class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans_list = []
        for i in nums:
            temp_list = [j for j in nums if j < i]
            if not temp_list:
                ans_list.append(0)
            else:
                ans_list.append(len(temp_list))
        return ans_list

if __name__ == "__main__":
    obj = Solution()
    _input = [8,1,2,2,3]
    answer = obj.smallerNumbersThanCurrent(_input)
    print(answer)