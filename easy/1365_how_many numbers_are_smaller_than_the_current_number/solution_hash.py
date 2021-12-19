class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        sort_nums = sorted(nums)
        
        # O(N)
        for index, num in enumerate(sort_nums):
            if num in hash_map:
                continue
            else:
                hash_map[num] = index
        # O(N)        
        for index, num in enumerate(nums):
            nums[index] = hash_map[num]
            
        return nums

if __name__ == "__main__":
    obj = Solution()
    _input = [8,1,2,2,3]
    answer = obj.smallerNumbersThanCurrent(_input)
    print(answer)