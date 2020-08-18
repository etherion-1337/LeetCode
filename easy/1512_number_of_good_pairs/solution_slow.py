from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > 1 :
            for i in range(1, len(nums)):
                if nums[0] == nums[i]:
                    count += 1
            nums.pop(0)

        return count


if __name__ == "__main__":
    soln = Solution()
    nums = [1,1,1,1]
    answer = soln.numIdenticalPairs(nums)
    print(answer)