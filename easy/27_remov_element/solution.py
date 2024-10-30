from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        old_len = len(nums)
        same_list = []
        for i in range(0, len(nums)):
            if nums[i] == val:
                count += 1
                same_list.append(i)

        # reverse the list to avoid index out of range
        # remove from the largest index
        same_list.reverse()

        for j in same_list:
            nums.pop(j)


        return old_len - count
    
class NeetSolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        maintain a pointer k to keep track of the position of the next element can be put there

        similar to 2 pointers, just that the apart from k, the moving pointer in the loop is i
        if nums[i] == val, we will skip it so that k is lagging behind i
        the next time nums[i] != val, we will put it at k
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k