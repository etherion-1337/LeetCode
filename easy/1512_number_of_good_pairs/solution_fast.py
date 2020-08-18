from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


if __name__ == "__main__":
    soln = Solution()
    nums = [1,1,1,1]
    answer = soln.numIdenticalPairs(nums)
    print(answer)