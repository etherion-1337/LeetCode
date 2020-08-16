from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return None
        else:
            for i in range(1, len(nums)):
                nums[i] += nums[i-1]
        return nums


if __name__ == "__main__":
    soln = Solution()
    num_list = [1,2,3,4]
    answer = soln.runningSum(num_list)
    print(answer)