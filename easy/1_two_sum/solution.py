from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        brute force
        time complexity: O(n^2)
        """
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if num_i + num_j == target and i != j:
                    return [i,j]
                
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        space complexity: O(n) or O(nums) -> stores hash table for nums
        time complexity: O(n) or O(nums) -> iterate through nums
        """
        hash_map = {}
        for index, num in enumerate(nums):
            _target = target - num
            if _target in hash_map:
                return [hash_map[_target], index]
            else:
                hash_map[num] = index

class NeetSolution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

