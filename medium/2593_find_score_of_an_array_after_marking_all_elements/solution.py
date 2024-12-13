from typing import List

class Solution:
    """
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    def findScore(self, nums: List[int]) -> int:
        rank = [i for i in range(len(nums))]
        rank.sort(key=lambda i: (nums[i], i))

        score = 0
        marked = [False] * len(nums)
        for r in rank:
            if marked[r] == False:
                score += nums[r]
                marked[r] = True
                if r - 1 >= 0:
                    marked[r - 1] = True
                if r + 1 < len(nums):
                    marked[r + 1] = True

        return score