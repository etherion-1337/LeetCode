from typing import List

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if j == i:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        time complexity: O(n)
        space complexity: O(1)
        """
        i = 0
        j = len(numbers) - 1

        while j > i:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            

class NeetSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]