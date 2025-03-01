from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        val = []
        zero = []
        zero_flag = False

        for i in range(len(nums) - 1):
            if zero_flag:
                cur = 0
            else:
                cur = nums[i]
            if cur == nums[i + 1]:
                zero_flag = True
                _cur = cur * 2
                if _cur == 0:
                    zero.append(_cur)
                else:
                    val.append(_cur)
            else:
                if cur == 0:
                    zero.append(cur)
                else:
                    val.append(cur)
                zero_flag = False

        if zero_flag or nums[-1] == 0:
            zero.append(0)
        else:
            val.append(nums[-1])

        return val + zero
    

class NeetSolution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # similiar to swapping in quicksort
        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums